# Student Ratings of Automatically Generated Questions Dataset

This directory contains the dataset and analysis code for our project
investigating factors influencing student ratings of automatically
generated questions, discussed in our paper

Johnson, B. G., Dittel, J. S., & Van Campenhout,
R. (2024). Investigating student ratings with features of
automatically generated questions: A large-scale analysis using data
from natural learning contexts. In B. Paaßen & C. D. Epp (Eds.),
*Proceedings of the 17th International Conference on Educational Data
Mining* (pp. 194–202). International Educational Data Mining
Society. [https://doi.org/10.5281/zenodo.12729796](https://doi.org/10.5281/zenodo.12729796)

We are pleased and honored to have won the [Best Paper
Award](https://educationaldatamining.org/edm2024/best-paper-awards/)
at [Educational Data Mining
2024](https://educationaldatamining.org/edm2024/) for this work! Thank
you, EDM!!

## Description

Integrating formative practice questions with short sections of course
content has been shown to increase student learning gains. However,
question writing is a labor-intensive process that requires both
subject matter and item writing expertise. The volume of questions
needed for a typical course is in the hundreds or thousands, a scale
that is often prohibitive in time and cost for manual development.

We are using automatic question generation (AQG) to lower this
barrier, using electronic textbooks as source material. To date,
approximately 2.5 million automatically generated (AG) questions have
been added to thousands of online textbooks in the VitalSource
Bookshelf ereader platform as a free study feature called CoachMe,
available to millions of students. There are several types of AG
questions available, including fill-in-the-blank (FITB), matching,
multiple choice, and free response.

As shown below, the questions open in a panel next to the textbook
content. As formative practice, students are allowed as many answer
attempts as they like, receive immediate feedback, and can also reveal
the answer if stuck. Students are able to rate questions after
answering with a social media-style :+1: or :-1:. These ratings are
the focus of the current study.

<p align="center">
<img alt="A FITB formative practice question in a chemistry textbook." src="./CoachMe_screenshot.png"/>
</p>

This project investigates relationships between student ratings and
the properties of AG questions. FITB questions, which are the majority
of the AG questions added to textbooks so far, are the focus of this
work. These questions are created by selecting important sentences
from textbook content and turning them into cloze questions by removing
an important word as a blank for the student to fill in.

The dataset for this study was compiled from student interactions
with FITB practice questions from January 1, 2022 to January 16,
2024, grouped into sessions consisting of all actions of an individual
student on an individual question. For each session, whether the
student gave a :+1: or :-1: rating (or neither) is noted. This
resulted in a dataset of 5,214,211 question sessions from natural
learning contexts. It is believed to be the largest of its kind to
date, involving 809,848 AG questions, 432,930 students, and 9,320
textbooks.

This dataset was used to build an explanatory model to evaluate ten
hypotheses about causal relationships affecting student rating
behavior. The hypotheses tested were:

Hypothesis | Description
-----------|------------
H1 | Answering a question correctly on the first attempt will increase the chance of a :+1: and decrease the chance of a :-1:.
H2 | As a student answers more questions, the chance of giving a :+1: or :-1: will decrease.
H3 | Receiving a spelling correction suggestion for an answer will increase the chance of a :+1: and decrease the chance of a :-1:.
H4 | Questions created from more important sentences in the textbook will receive more :+1: and fewer :-1:.
H5 | Questions with answer words that are more important in the textbook will receive more :+1: and fewer :-1:.
H6 | Questions with noun and adjective answer words will receive more :+1: and fewer :-1: than verb and adverb answer words.
H7 | Questions with rarer words as the answer will receive more :+1: and fewer :-1: than questions with more common words as the answer.
H8 | Questions where the answer blank occurs early in the sentence will receive fewer :+1: and more :-1:.
H9 | Questions that give elaborative feedback after an incorrect answer will receive more :+1: and fewer :-1: than questions that give only outcome feedback.
H10 | Questions that have been reviewed by a human reviewer before inclusion will receive more :+1: and fewer :-1: than questions that did not have human review.


Each hypothesis was operationalized with a variable from the session
data and AG question characteristics for inclusion in the explanatory
model. Mixed effects logistic regression was used to model the
probability of whether a student will rate a question :+1: or :-1: as
a function of these explanatory variables. In the explanatory modeling
framework followed, a statistically significant relationship between
an explanatory variable and a rating outcome provides evidence that
the relationship in the corresponding hypothesis is causal.

Further details can be found in the paper above.

## Data Files and Code Notebooks

The files provided are:

File | Description
-----|------------
sessions.parquet | Student sessions dataset
Student Ratings of Automatically Generated Questions Analysis.ipynb | Jupyter notebook for student ratings analysis

The sessions data file is in Apache Parquet format. The Python code
example below loads the sessions data into a pandas dataframe:

```
import pandas as pd
sessions = pd.read_parquet( 'sessions.parquet' )
```

The fields in the dataset are:

Field | Type | Definition
------|------|-----------
`student_id` | string | Anonymized student identifier
`question_id` | string | Question identifier
`thumbs_up` | categorical | 1 if student gave the question a :+1: rating, 0 if not
`thumbs_down` | categorical | 1 if student gave the question a :-1: rating, 0 if not
`H1_first_correct` | categorical | 1 if student’s first answer is correct, 0 if not
`H2_cumulative_answered` | integer | Total number of questions answered by the student so far
`H3_spelling_suggestion` | categorical | 1 if student received a spelling suggestion during the session, 0 if not
`H4_sentence_textrank_rank` | continuous | 0 (most important) to 1 (least important) rank of sentence in textbook chapter
`H5_answer_tf_idf_rank` | continuous | 0 (most important) to 1 (least important) rank of answer word in textbook chapter
`H6_answer_pos` | categorical | `ADJ`, `ADV`, `NOUN`, `PROPN`, `VERB`
`H7_answer_log_probability` | continuous | Log probability estimate of answer word frequency
`H8_answer_location` | integer | Location of answer blank in sentence, starting at 0 for first word
`H9_feedback` | categorical | `common_answer`, `context`, `outcome`
`H10_reviewed` | categorical | 1 if question was manually reviewed, 0 if not

The Jupyter notebook provided contains Python and R code for
reproducing the results given in the paper.

## Contact Us

If you have questions, please feel free to email benny.johnson@vitalsource.com.
