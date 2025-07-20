import argparse
import os
import re

import openai
import pandas as pd


openai.api_key = os.getenv( "OPENAI_API_KEY" )
model_name = "gpt-4o-mini"


def get_message( content, role="user" ):
    assert role in [ "system", "user", "assistant" ], f'Bad role: "{role}"'
    return { "role": role, "content": content }


def get_completion( messages, temperature ):
    assert messages[ 0 ][ "role" ] == "system"
    assert len( messages ) > 1
    for m1, m2 in zip( messages, messages[ 1: ] ):
        assert m1[ "role" ] != m2[ "role" ], ( m1[ "role" ], m2[ "role" ] )
    completion = openai.ChatCompletion.create(
        model=model_name, temperature=temperature, messages=messages, seed=42
    )
    return completion.choices[ 0 ].message.content


def get_role():
    role = "You are a college professor. You are an excellent teacher and an expert at writing questions to help your students learn."
    return role


def get_explain_answer_selection_prompt( sentence, title ):
    prompt = f"""I'd like you to help me make a fill-in-the-blank question to help students learn. I will give you a sentence from a textbook
and I want you to create a question from it by replacing one word from the sentence with a blank for the student to fill in.
The title of the textbook is "{title}". The sentence is

"{sentence}"
"""
    prompt += """
Please select the best word to use as the blank. Think step by step.
Print the question you created in a <question> tag and the answer you selected in an <answer> tag."""
    return prompt


def _clean_question( sentence, question, answer ):
    # Find occurrence of answer closest to blank.
    sub_sentence = re.sub( "_+", answer, question )
    len_difference = max( len( sub_sentence ) - len( sentence ), 0 )
    pos = max( question.find( "__" ) - len_difference, 0 )
    offset = sentence[ pos: ].find( answer )
    assert offset != -1
    pos = offset + pos
    # Standardize blank length.
    BLANK = "______"
    question = sentence[ :pos ] + BLANK + sentence[ pos + len( answer ) : ]
    assert question.replace( BLANK, answer ) == sentence
    return question


def _ambiguate_blank( question ):
    if question.startswith( "A __" ):
        question = "A(n) __" + question[ 4: ]
        return question
    if question.startswith( "An __" ):
        question = "A(n) __" + question[ 5: ]
        return question
    pos = question.find( " a __" )
    if pos != -1:
        question = question[ :pos ] + " a(n) __" + question[ pos + 5 : ]
        return question
    pos = question.find( " an __" )
    if pos != -1:
        question = question[ :pos ] + " a(n) __" + question[ pos + 6 : ]
        return question
    return question


def generate_llm_question( sentence, prompt, verbose=False ):
    messages = [ get_message( get_role(), "system" ), get_message( prompt ) ]
    completion = get_completion( messages, temperature=0.0 )
    if verbose:
        print( completion )
    question = (
        re.search( r"<question>(.*?)</question>", completion, re.DOTALL )
        .group( 1 )
        .strip()
    )
    answer = (
        re.search( r"<answer>(.*?)</answer>", completion, re.DOTALL ).group( 1 ).strip()
    )
    question = _clean_question( sentence, question, answer )
    question = _ambiguate_blank( question )
    return question, answer


def generate_llm_questions( question_data ):
    llm_stem_col = "llm_stem"
    llm_answer_col = "llm_answer"
    if llm_stem_col not in question_data.columns:
        question_data[ llm_stem_col ] = None
        question_data[ llm_answer_col ] = None
    print( 'Generating', question_data[ llm_stem_col ].isna().sum(), 'of', len( question_data ), 'questions...' )
    for i_question, row in enumerate( question_data.itertuples(), 1 ):
        print( f"=== Question {i_question} of {len(question_data)} ===" )
        idx = row.Index
        if question_data.loc[ idx, llm_stem_col ] is not None:
            continue
        sentence = row.sentence
        title = row.title
        print( title )
        print( sentence )
        prompt = get_explain_answer_selection_prompt( sentence, title )
        try:
            llm_question, llm_answer = generate_llm_question(
                sentence, prompt, verbose=True
            )
            same = llm_question == row.stem
            print( "Original answer:", row.answer )
            print(
                "LLM answer:     ",
                llm_answer,
                "SAME BLANK" if same else "DIFFERENT BLANK",
            )
            question_data.loc[ idx, llm_stem_col ] = llm_question
            question_data.loc[ idx, llm_answer_col ] = llm_answer
        except Exception as e:
            print( "*** FAILED ***" )
            print( e )
        print( "*" * 120 )
        if i_question % 100 == 0:
            print( 'Saving backup...' )
            question_data.to_parquet( f'{question_data_fn}_bak' )
            print( "*" * 120 )


parser = argparse.ArgumentParser()
parser.add_argument( "question_data_fn", help="question data filename" )
args = parser.parse_args()
question_data_fn = args.question_data_fn
print( 'Question data file:', question_data_fn )

question_data = pd.read_parquet( question_data_fn )

generate_llm_questions( question_data )
question_data[ "H11_llm_aligned" ] = question_data[ "llm_stem" ] == question_data.stem

question_data.to_parquet( question_data_fn )
