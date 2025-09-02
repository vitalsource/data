import argparse
import os
import re

import openai
import pandas as pd

# Ensure OPENAI_API_KEY environment variable is correctly set
openai.api_key = os.getenv( 'OPENAI_API_KEY' )
assert openai.api_key, 'OPENAI_API_KEY environment variable is not set'

model_name = 'gpt-4o-mini'


def get_professor_role_description():
    role = 'You are a college professor. You are an excellent teacher and an expert at writing questions to help your students learn and assessing their answers.'
    return role


def format_message( content, role='user' ):
    assert role in [ 'system', 'user', 'assistant' ], f'Bad role: "{role}"'
    return { 'role': role, 'content': content }


def fetch_openai_completion( messages, temperature ):
    assert messages[ 0 ][ 'role' ] == 'system'
    assert len( messages ) > 1
    for m1, m2 in zip( messages, messages[ 1: ] ):
        assert m1[ 'role' ] != m2[ 'role' ], ( m1[ 'role' ], m2[ 'role' ] )
    completion = openai.ChatCompletion.create(
        model=model_name, temperature=temperature, messages=messages, seed=42
    )
    return completion.choices[ 0 ].message.content


def create_cc_assessment_prompt( question, answer, feedback ):
    prompt = f'''I will give you a student's answer to a question and feedback on the answer from their professor. Please do the following:

1. Determine if the student made a genuine attempt to answer the question. Consider both the answer and the professor's feedback.
   Label the answer as genuine if it meaningfully engages with the terms from the question, even if incomplete or incorrect.
   If the answer does not address the question terms or seems irrelevant, label it as not genuine.
2. Determine if the student's answer is correct. Likewise, consider both the answer and the professor's feedback to decide.
     * If the answer is not genuine, of course it's not correct.
     * When the answer is completely off the mark or fundamentally flawed the professor tends to provide a good answer as an example instead of directly addressing the student's answer.
     * Deciding correctness can sometimes be a gray area, so use a standard of whether a college professor would reasonably consider the answer complete and correct.
3. Explain your reasoning.
4. Output the decisions from 1 and 2 in the following format. Check that the format is correct before printing.
<genuine>True/False</genuine>
<correct>True/False</correct>

Question: {question}
Answer: {answer}
Feedback: {feedback}
'''
    return prompt


def evaluate_cc_answer( prompt, verbose=False ):
    messages = [ format_message( get_professor_role_description(), 'system' ), format_message( prompt ) ]
    completion = fetch_openai_completion( messages, temperature=0.0 )
    if verbose:
        print( completion )
    genuine = { 'true': True, 'false': False }[ re.search( r'<genuine>(.*?)</genuine>', completion ).group( 1 ).lower() ]
    correct = { 'true': True, 'false': False }[ re.search( r'<correct>(.*?)</correct>', completion ).group( 1 ).lower() ]
    if not genuine and correct:
        print( 'WARNING: Non-genuine and correct' )
        print( prompt )
        print( completion )
    return genuine, correct


def categorize_cc_answers( event_data ):
    if 'genuine' not in event_data.columns:
        event_data[ 'genuine' ] = None
        event_data[ 'correct' ] = None
    print( 'Assessing', event_data[ 'correct' ].isna().sum(), 'of', len( event_data ), 'events...' )
    for i_row, row in enumerate( event_data.itertuples(), 1 ):
        if row.event_type != 'enhanced_question':
            continue
        idx = row.Index
        if event_data.loc[ idx, 'correct' ] is not None:
            continue
        print( f'=== Event {i_row} of {len(event_data)} ===' )
        question = row.question
        answer = row.answer.strip()
        feedback = row.feedback.strip()
        prompt = create_cc_assessment_prompt( question, answer, feedback )
        try:
            genuine, correct = evaluate_cc_answer( prompt, verbose=True )
            print( 'Question:', question )
            print( 'Answer:  ', answer )
            print( 'Feedback:', feedback )
            print( 'Genuine: ', genuine, 'Correct: ', correct )
            event_data.loc[ idx, 'genuine' ] = genuine
            event_data.loc[ idx, 'correct' ] = correct
        except Exception as e:
            print( '*** FAILED ***' )
            print( e )
        print( '*' * 120 )
        if i_row % 100 == 0:
            print( 'Saving backup...' )
            event_data.to_parquet( f'{event_data_fn}_bak' )
            print( '*' * 120 )

    # Add attempt_category based on correct and genuine columns
    event_data[ 'attempt_category' ] = event_data.apply(
        lambda row: '+' if row[ 'correct' ] else '-' if row[ 'genuine' ] else 'x',
        axis=1
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument( 'event_data_fn', help='event data filename' )
    args = parser.parse_args()

    event_data_fn = args.event_data_fn
    print( 'Event data file:', event_data_fn )
    event_data = pd.read_parquet( event_data_fn )
    categorize_cc_answers( event_data )
    event_data.to_parquet( event_data_fn )
