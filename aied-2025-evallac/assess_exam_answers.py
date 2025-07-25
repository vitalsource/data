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
    role = "You are a college professor. You are an excellent teacher and an expert at writing questions to help your students learn and assessing their answers."
    return role


def get_assess_ecm_exam_question_answer_prompt( question, answer, feedback ):
    prompt = f"""A student was asked to write an exam question for a section in their textbook as a study activity. Their professor then gave
them feedback on it. I will give you the student's question and the professor's feedback. Please do the following:

1. Determine if the student made a genuine attempt. Consider both the exam question and the professor's feedback.
   To be genuine, both of the following must be true:
     * The student's question must engage with a key concept of the section.
     * It must attempt to assess something meaningful about a student's knowledge of the section.
   If either condition is not satisfied, label the attempt as not genuine:
2. Determine if the student's attempt is acceptable. Likewise, consider both the exam question and the professor's feedback to decide.
     * If the attempt is not genuine, of course it's not acceptable.
     * It doesn't have to be a comprehensive question about the section (few actual exam questions are).
     * It doesn't necessarily have to be difficult, broad, or require deeper thinking to be acceptable. A simple question on a single topic will do if a student would have to understand something meaningful about the section to answer it.
     * The professor tends to give constructive criticism on how the student's exam question could be improved by making it broader or more comprehensive, but that in itself doesn't make it unacceptable. If it's not fundamentally flawed or irrelevant, it's acceptable.
3. Explain your reasoning.
4. Output the decisions from 1 and 2 in the following format. Check that the format is correct before printing.
<genuine>True/False</genuine>
<acceptable>True/False</acceptable>

Activity: {question}
Exam Question: {answer}
Feedback: {feedback}
"""
    print(prompt)
    return prompt


def assess_ecm_exam_question_answer( prompt, verbose=False ):
    messages = [ get_message( get_role(), "system" ), get_message( prompt ) ]
    completion = get_completion( messages, temperature=0.0 )
    if verbose:
        print( completion )
    # Sometimes ending tag is mismatched, but beginning tag seems to always be OK.
    genuine = { 'true': True, 'false': False }[ re.search( r"<genuine>(.*?)</", completion ).group( 1 ).lower() ]
    correct = { 'true': True, 'false': False }[ re.search( r"<acceptable>(.*?)</", completion ).group( 1 ).lower() ]
    if not genuine and correct:
        print( 'WARNING: Non-genuine and acceptable' )
        print( prompt )
        print( completion )
    return genuine, correct


def assess_ecm_answers( question_data ):
    if 'genuine' not in question_data.columns:
        question_data[ 'genuine' ] = None
    if 'correct' not in question_data.columns:
        question_data[ 'correct' ] = None
    print( 'Assessing', question_data[ 'correct' ].isna().sum(), 'of', len( question_data ), 'events...' )
    for i_row, row in enumerate( question_data.itertuples(), 1 ):
        # Skip non-answer events, e.g., ratings
        if row.event_type != 'enhanced_question':
            continue
        idx = row.Index
        if question_data.loc[ idx, 'correct' ] is not None:
            continue
        print( f"=== Event {i_row} of {len(question_data)} ===" )
        question = row.question
        answer = row.answer.strip()
        feedback = row.feedback.strip()
        prompt = get_assess_ecm_exam_question_answer_prompt( question, answer, feedback )
        try:
            genuine, correct = assess_ecm_exam_question_answer(
                prompt, verbose=True
            )
            print( 'Question:', question )
            print( 'Answer:  ', answer )
            print( 'Feedback:  ', feedback )
            print( 'Genuine: ', genuine, 'Correct: ', correct )
            question_data.loc[ idx, 'genuine' ] = genuine
            question_data.loc[ idx, 'correct' ] = correct
        except Exception as e:
            print( "*** FAILED ***" )
            print( e )
        print( "*" * 120 )
        if i_row % 100 == 0:
            print( 'Saving backup...' )
            question_data.to_parquet( f'{question_data_fn}_bak' )
            print( "*" * 120 )


parser = argparse.ArgumentParser()
parser.add_argument( "question_data_fn", help="question data filename" )
args = parser.parse_args()
question_data_fn = args.question_data_fn
print( 'Question data file:', question_data_fn )

question_data = pd.read_parquet( question_data_fn )
print( len( question_data ) )

assess_ecm_answers( question_data )

question_data.to_parquet( question_data_fn )
