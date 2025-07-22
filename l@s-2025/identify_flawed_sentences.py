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


def get_completion( messages, **kwargs ):
    assert messages[ 0 ][ 'role' ] == 'system'
    assert len( messages ) > 1
    for m1, m2 in zip( messages, messages[ 1: ] ):
        assert m1[ 'role' ] != m2[ 'role' ], ( m1[ 'role' ], m2[ 'role' ] )
    completion = openai.ChatCompletion.create(
        model=model_name,
        messages=messages,
        seed=42,
        **kwargs
    )
    return completion.choices[ 0 ].message.content


def get_role():
    role = f"""You are a domain-agnostic college-level educator and question-design expert.
Students reading these sentences already have the course background to understand
typical concepts. Your job is to decide whether a single textbook sentence is
suitable for making a fill-in-the-blank question.

IMPORTANT GUIDELINE: If you are uncertain or if the sentence at least conveys
some useful concept, do NOT label it as flawed. Only label a sentence flawed
if it clearly meets a major-flaw criterion."""
    return role


def get_assess_sentence_prompt( sentence ):
    prompt = f"""Below is a single textbook sentence.

Decide if it has a MAJOR FLAW that makes it unsuitable for a fill-in-the-blank question.

A sentence has a MAJOR FLAW (label “YES: reason”) only if ANY of these conditions apply:
1) **Purely Structural or Directive**:
   - The entire sentence just references external text or future/previous sections (“see Section 2,” 
     “as shown above,” “in the next chapter…”) without stating an actual fact or concept.
2) **Extremely Vague or Trivial**:
   - The sentence offers no meaningful claim or relationship (e.g., “Things happen,” 
     “We need more data,” “One explanation is possible” without saying what it explains).
3) **Local Scenario Lacking Broader Meaning**:
   - The sentence describes individuals or events that a typical domain student cannot interpret 
     without extra text. (A purely anecdotal snippet: “Joyce accused potheads of being immoral.”)
   - Merely naming real events, people, or dates is NOT a flaw if the sentence still conveys 
     a testable point or concept.
4) **Depends Entirely on a Figure or Table**:
   - The sentence’s main claim is “As shown in Figure X” or “see Table Y” with no self-contained fact.

If the sentence does NOT clearly meet any of the above flaws, label it:
NO: <short reason>

**When in doubt, do NOT label it flawed.**

---

### Real Examples

#### Flawed (YES)

1) *Business & Economics: Meeting the Ethical Challenges of Leadership*  
"Joyce hasn't helped matters by accusing the marijuana store supporters (whom she referred to as 'potheads') of being immoral."  
**Answer**: YES: local anecdote with no generalizable fact or concept.

2) *Psychology: Social Psychology*  
"One explanation is that the risk of rejection is much greater."  
**Answer**: YES: extremely vague; we don’t know what is being explained.

3) *Political Science: The Essentials of Political Analysis*  
"For a discussion of how the construct validity approach has been applied to the Graduate Record Examination, see Janet Buttolph Johnson and H. T. Reynolds…"  
**Answer**: YES: purely directive, no self-contained fact.

---

#### Not Flawed (NO)

1) *Political Science: American Government*  
"A redrawn map—done so following the 2020 census, and under the leadership of the Democrat-controlled New Mexico state government—was prepared to dramatically and intentionally reshape the boundaries of both Herrell's and Leger Fernández's districts."  
**Answer**: NO: Though it references real districts and a local event, it conveys a testable idea about redistricting.

2) *Social Science: Fair Play*  
"As a result of our childhood experiences, many of us become participants and retain some affiliation with sports for life, even if only as spectators."  
**Answer**: NO: There is a clear concept (childhood → lifelong sports affiliation).

3) *Art: Cinematography: Theory and Practice*  
"Cutaways may emphasize some action in the scene, provide additional information, or be something that the character looks at or points to."  
**Answer**: NO: Explains a general filmmaking concept about cutaways.

4) *Business & Economics: Persuasion in Your Life*  
"Relevance may seem like an obvious standard for a persuasive argument."  
**Answer**: NO: States a principle (relevance as a standard in persuasion), which a student could be quizzed on.

---

**Now classify this sentence**:
“{sentence}”
"""
    return prompt


def assess_sentence( sentence, prompt, verbose=False ):
    messages = [ get_message( get_role(), "system" ), get_message( prompt ) ]
    completion = get_completion( messages, temperature=0, top_p=1, max_tokens=50 )
    if verbose:
        print( completion )
    assert completion.startswith( 'YES:' ) or completion.startswith( 'NO:' )
    flawed = completion.startswith( 'YES:' )
    return flawed


def assess_sentences( question_data ):
    llm_assess_col = f"flawed"
    if llm_assess_col not in question_data.columns:
        question_data[ llm_assess_col ] = None
    print( 'Assessing', question_data[ llm_assess_col ].isna().sum(), 'of', len( question_data ), 'sentences...' )
    for i_question, row in enumerate( question_data.itertuples(), 1 ):
        idx = row.Index
        if question_data.loc[ idx, llm_assess_col ] is not None:
            continue
        print( f"=== Sentence {i_question} of {len(question_data)} ===" )
        sentence = row.sentence
        vbid = row.vbid
        subject = row.subject
        print( f'{subject}: ({vbid})' )
        print( sentence )
        prompt = get_assess_sentence_prompt( sentence )
        try:
            flawed = assess_sentence(
                sentence, prompt, verbose=True
            )
            print(
                "Flawed:     ", flawed,
            )
            question_data.loc[ idx, llm_assess_col ] = flawed
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

assess_sentences( question_data )

question_data.to_parquet( question_data_fn )
