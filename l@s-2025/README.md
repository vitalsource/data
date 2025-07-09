# LLM-Assisted Sentence Selection for Cloze Question Generation Dataset

This directory contains the dataset and analysis code for our project
investigating the effectiveness of using large language models (LLMs)
as a filter to identify unsuitable sentences for automatic
fill-in-the-blank (FITB) cloze question generation, as discussed in
our paper:

Dittel, J. S., Van Campenhout, R., & Johnson, B. G. (2025). Refining
sentence selection for automatic cloze question generation with large
language models. In _Proceedings of the Twelfth ACM Conference on
Learning at Scale (L@S '25)_, Palermo,
Italy. https://doi.org/10.1145/3698205.3733926, **pp. TODO: add page
numbers when available**

## Description

Formative practice embedded within textbooks has been shown to
increase learning outcomes. However, manually authoring high-quality
formative practice questions is resource-intensive and impractical at
scale. Recent advances in automatic question generation (AQG) have
enabled large-scale creation of formative practice questions.

Building on these advances, we have introduced CoachMe, a free study
feature integrated into the VitalSource Bookshelf ereader
platform. CoachMe delivers formative practice through automatically
generated (AG) questions placed directly within electronic
textbooks. AG questions have already been added to thousands of
textbooks, serving millions of students. CoachMe supports several
question types, including FITB, matching, multiple choice, and free
response.

As shown below, CoachMe questions appear in a panel next to the
textbook content. Students can make unlimited attempts, receive
immediate feedback, and reveal answers if needed. They can also rate
questions after answering with a social media-style 👍 or 👎, and
these ratings are the specific focus of this dataset.

<p align="center">
<img alt="A FITB formative practice question in a chemistry textbook." src="./CoachMe_screenshot.png"/>
</p>

This study specifically investigates whether integrating an LLM-based
filter into an existing rule-based AQG pipeline can identify sentences
unsuitable for cloze question generation. By detecting sentences
likely to yield low-quality questions, the goal is to reduce student
dissatisfaction (👎 ratings). The hypothesis is that the LLM's
semantic understanding can better pinpoint sentences likely to produce
poor questions, thus improving the overall quality of automatically
generated FITB questions.

Drawing on an explanatory modeling framework, this project assesses
whether students are more likely to give a 👎 rating when the
underlying sentence was flagged by the LLM as unsuitable. Research
consistently indicates that positive student perceptions correlate
strongly with enhanced engagement, motivation, and persistence in
learning tasks. Therefore, successful LLM-based sentence screening
could improve large-scale formative practice by discarding confusing
or irrelevant items, helping the question generation pipeline produce
more effective FITB cloze questions.

The dataset for this analysis is a subset of a [previously released
dataset](https://github.com/vitalsource/data/tree/aied-2025-itextbooks/edm-2024),
specifically focused on FITB cloze question interactions recorded
between January 1, 2022, and January 16, 2024. Student-question
sessions were formed by grouping all actions of a single student on a
single question. Filtering for publishers granting permission for
generative AI research resulted in a dataset comprising 1,305,957
sessions across 210,902 questions, 106,183 students, and 2,510
textbooks, predominantly from the Social Science, Psychology, and
Political Science domains.

Eleven hypotheses were tested, with hypotheses H1–H10 validated in
earlier work and included here as control variables, and hypothesis
H11 newly introduced as the primary focus of this analysis:

| Hypothesis | Description |
|------------|-------------|
| H1 | Answering a question correctly on the first attempt will decrease the chance of a 👎. |
| H2 | As a student answers more questions, the chance of giving a 👎 will decrease. |
| H3 | Receiving a spelling correction suggestion for an answer will decrease the chance of a 👎. |
| H4 | Questions created from more important sentences in the textbook will receive fewer 👎. |
| H5 | Questions with answer words that are more important in the textbook will receive fewer 👎. |
| H6 | Questions with noun and adjective answer words will receive fewer 👎 than verb and adverb answer words. |
| H7 | Questions with rarer words as the answer will receive fewer 👎 than questions with more common words as the answer. |
| H8 | Questions where the answer blank occurs early in the sentence will receive more 👎. |
| H9 | Questions providing elaborative feedback after an incorrect answer will receive fewer 👎 than questions providing only outcome feedback. |
| H10 | Questions reviewed by a human before inclusion will receive fewer 👎 than those without human review. |
| **H11** | **Questions derived from sentences flagged by the LLM as unsuitable will receive more 👎 than questions derived from sentences that were not flagged.** |

Mixed effects logistic regression modeling was used to test whether
sentences flagged by the LLM as unsuitable (H11) were more likely to
receive negative student feedback (👎), controlling for previously
validated explanatory variables (H1–H10). In the explanatory modeling
framework followed, a statistically significant relationship between
an explanatory variable and a rating outcome provides evidence that
the relationship in the corresponding hypothesis is causal.

Further details can be found in the paper above.

## Data Files and Analysis Code

The files provided are:

| File | Description |
|------|-------------|
| `sessions.parquet` | Student-question sessions dataset |
| `questions.parquet` | Question-level dataset including text and aggregated interaction data |
| `identify_flawed_sentences.py` | Prompt and code used for LLM sentence filtering |
| `Sentence Selection Analysis.ipynb` | Jupyter notebook for replication of data analysis in the paper |

The sessions dataset includes the following fields:

| Field | Type | Definition |
|-------|------|------------|
| `student_id` | string | Anonymized student identifier |
| `question_id` | string | Unique question identifier |
| `textbook_id` | string | Unique textbook identifier |
| `subject` | string | Textbook's BISAC major subject heading (e.g., "Social Science") |
| `thumbs_down` | categorical | 1 if student gave the question a 👎 rating, 0 otherwise |
| `H1_first_correct` | categorical | 1 if student's first answer is correct, 0 otherwise |
| `H2_cumulative_answered` | integer | Total number of questions answered by the student up to the session |
| `H3_spelling_suggestion` | categorical | 1 if student received a spelling suggestion, 0 otherwise |
| `H4_sentence_textrank_rank` | continuous | Sentence importance ranking within textbook chapter (0=most important to 1=least important) |
| `H5_answer_tf_idf_rank` | continuous | Importance ranking of the answer word within textbook chapter (0=most important to 1=least important) |
| `H6_answer_pos` | categorical | Part of speech of answer word (`ADJ`, `ADV`, `NOUN`, `PROPN`, `VERB`) |
| `H7_answer_log_probability` | continuous | Log probability estimate of answer word frequency |
| `H8_answer_location` | integer | Position of answer blank in the sentence (0=first word) |
| `H9_feedback` | categorical | Type of feedback given (`common_answer`, `context`, `outcome`) |
| `H10_reviewed` | categorical | 1 if question was manually reviewed, 0 otherwise |
| `H11_llm_rejected` | categorical | 1 if LLM flagged the sentence as unsuitable, 0 otherwise |

The questions dataset includes the following fields:

| Field | Type | Definition |
|-------|------|------------|
| `question_id` | string | Unique question identifier |
| `textbook_id` | string | Unique textbook identifier |
| `subject` | string | Textbook's BISAC major subject heading (e.g., "Social Science") |
| `students` | integer | Number of unique students who interacted with the question |
| `thumbs_down` | integer | Total number of 👎 ratings for the question |
| `stem` | string | Text of the question with a blank to fill in |
| `answer` | string | Correct answer to the question |
| `sentence` | string | Original sentence from which the question was derived |
| `H11_llm_rejected` | categorical | 1 if LLM flagged the sentence as unsuitable, 0 otherwise |

## Acknowledgments

We thank the following publishers for granting permission to release
automatically generated questions derived from their textbooks as part
of this open dataset:

- OpenStax
- SAGE Publications
- Taylor & Francis

## Contact Us

If you have questions, please feel free to email benny.johnson@vitalsource.com.
