# Automatically Generated and Human-Authored Question Performance Dataset

This directory contains the complete dataset and analysis code for
our project comparing performance of automatically generated and
human-authored questions, which is discussed in our papers

Van Campenhout, R., Brown, N., Jerome, B., Dittel, J. S., & Johnson,
B. G. (2021). Toward effective courseware at scale: Investigating
automatically generated questions as formative practice. In
*Proceedings of the Eighth ACM Conference on Learning@Scale*
(pp. 295–298). ACM. [https://doi.org/10.1145/3430895.3460162](https://doi.org/10.1145/3430895.3460162)

Van Campenhout, R., Dittel, J. S., Jerome, B., & Johnson,
B. G. (2021). Transforming textbooks into learning by doing
environments: An evaluation of textbook-based automatic question
generation. In *Proceedings of the Third Workshop on Intelligent
Textbooks at the 22nd International Conference on Artificial
Intelligence in Education* (pp. 60–73). CEUR Workshop
Proceedings. [http://ceur-ws.org/Vol-2895/paper06.pdf](http://ceur-ws.org/Vol-2895/paper06.pdf)

We are pleased and honored to have won the first ever Learning@Scale
Best Open Data Set Paper Award for this work! Thank you,
[L@S](https://learningatscale.acm.org) and [Schmidt
Futures](https://schmidtfutures.com)!!
https://twitter.com/LearningAtScale/status/1408112524134846466

## Description

Integrating formative practice questions with short sections of lesson
content has been shown to increase student learning gains. However,
question writing is a labor-intensive process that requires both
subject matter and item writing expertise. The volume of questions
needed for a typical course is in the hundreds or thousands, a scale
that is often prohibitive in time and cost for manual development. We
are investigating automatic question generation (AQG) as a way to
reduce this barrier, using textbooks as the source material.

The dataset made available is from an ongoing project to evaluate the
quality of textbook-based AQG in a variety of natural learning
contexts. Data are provided from six college courses that used
textbook-based courseware environments, in which automatically
generated (AG) questions were included alongside human-authored (HA)
questions and answered by the same student cohorts. Observations of AG
and HA questions were recorded on three performance metrics relevant
to formative practice: engagement, difficulty, and persistence.

* Engagement: Whether a student chooses to answer a question encountered on a lesson page.
* Difficulty: Whether a student answers a question correctly on the first attempt.
* Persistence: Whether a student continues to answer a question until correct when the first attempt is incorrect.

We believe this dataset, containing 786,242 total observations of
student-question interactions in natural learning contexts, to be the
largest of its kind to date, useful for gaining insights into the
potential for AQG to enhance textbook content.

Course | Students | AG Questions | HA Questions | Engagement<br/>Observations | Difficulty<br/>Observations | Persistence<br/>Observations
-------|----------|--------------|--------------|-----------------------------|-----------------------------|-----------------------------
Neuroscience | 516 | 747 | 888 | 286,129 | 120,098 | 34,124
Communication A | 109 | 263 | 390 | 43,538 | 20,990 | 5,643
Microbiology | 99 | 416 | 690 | 71,119 | 42,114 | 10,520
Psychology | 91 | 607 | 48 | 34,757 | 29,583 | 4,926
Communication B | 79 | 386 | 533 | 35,351 | 17,547 | 4,806
Accounting | 51 | 191 | 403 | 14,661 | 8,309 | 2,027

Further details can be found in the paper above.

## Data Files and Code Notebooks

The files provided are:

File | Description
-----|------------
engagement_neuroscience.txt | Engagement dataset for the Neuroscience course
engagement_communication_a.txt | Engagement dataset for the Communication A course
engagement_microbiology.txt | Engagement dataset for the Microbiology course
engagement_psychology.txt | Engagement dataset for the Psychology course
engagement_communication_b.txt | Engagement dataset for the Communication B course
engagement_accounting.txt | Engagement dataset for the Accounting course
difficulty_neuroscience.txt | Difficulty dataset for the Neuroscience course
difficulty_communication_a.txt | Difficulty dataset for the Communication A course
difficulty_microbiology.txt | Difficulty dataset for the Microbiology course
difficulty_psychology.txt | Difficulty dataset for the Psychology course
difficulty_communication_b.txt | Difficulty dataset for the Communication B course
difficulty_accounting.txt | Difficulty dataset for the Accounting course
persistence_neuroscience.txt | Persistence dataset for the Neuroscience course
persistence_communication_a.txt | Persistence dataset for the Communication A course
persistence_microbiology.txt | Persistence dataset for the Microbiology course
persistence_psychology.txt | Persistence dataset for the Psychology course
persistence_communication_b.txt | Persistence dataset for the Communication B course
persistence_accounting.txt | Persistence dataset for the Accounting course
Question Engagement Analysis.ipynb | Jupyter notebook for engagement regression analysis
Question Difficulty Analysis.ipynb | Jupyter notebook for difficulty regression analysis
Question Persistence Analysis.ipynb | Jupyter notebook for persistence regression analysis

Data files are tab-delimited with one observation per line. The fields in the data files are:

Field | Description
------|------------
`student` | Anonymized student identifier
`question` | Question identifier
`course_page_number` | Location of the question’s page within the course
`unit_page_number` | Location of the question’s page within its course unit
`module_page_number` | Location of the question’s page within its course module
`page_question_number` | Question’s number on its page
`question_type` | Identifier for question origin and format<br/>Examples:<br/>`AG_FITB` = automatically generated fill-in-the-blank<br/>`HA_MC` = human-authored multiple-choice
`answered` | Whether the student answered the question (for engagement)
`correct` | For answered questions, whether the student got the correct answer on the first attempt (for difficulty)
`persisted` | For incorrectly answered questions, whether the student continued to answer the question until they got the correct answer (for persistence)

Location-based variables (e.g., `course_page_number`) are provided
since these are also known to impact student engagement. These are
included as covariates in the regression analyses. Not all courses
divided their units into modules. For these, `unit_page_number` and
`module_page_number` are dependent, so `R` gives the message
`fixed-effect model matrix is rank deficient so dropping 1 column /
coefficient` when fitting the regression models.

## Contact Us

If you have questions, please feel free to email benny.johnson@vitalsource.com.
