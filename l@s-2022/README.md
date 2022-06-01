# Automatically Generated and Human-Authored Question Discrimination Data Set

This folder contains the complete data set for our study comparing
discrimination of automatically generated and human-authored
questions, which is discussed in our paper

Johnson, B. G., Dittel, J. S., Van Campenhout, R., & Jerome, B. (2022).
Discrimination of Automatically Generated Questions Used as Formative
Practice. L@S '22: Proceedings of the Ninth ACM Conference on
Learning@Scale, pp. 325-329. https://doi.org/10.1145/3491140.3528323

## Description

Integrating formative practice questions with short sections of lesson
content has been shown to increase student learning gains. However,
question writing is a labor-intensive process that requires both
subject matter and item writing expertise. The volume of questions
needed for a typical course is in the hundreds or thousands, a scale
that is often prohibitive in time and cost for manual development. We
are investigating automatic question generation (AQG) as a way to
reduce this barrier, using textbooks as the source material.

The data set made available is from an ongoing project to evaluate the
quality of textbook-based AQG in a variety of natural learning
contexts. The present study builds on our previous work in which we
found found that automatically generated (AG) and human-authored (HA)
questions performed similarly on measures of engagement, difficulty,
and persistence
(https://github.com/vitalsource/data/tree/main/l@s-2021). Here, we
extend the investigation to discrimination, an important psychometric
property and measure of question quality, using student data for AG
and HA questions in a courseware environment from a university
Neuroscience course.

Discrimination is the concept of how well a question can distinguish
between high-ability and low-ability students. The greater a
question's discrimination, the more likely a correct answer indicates
that the student has a higher ability and that an incorrect answer
indicates a lower ability. Conversely, low discrimination means the
correctness of the answer is less indicative of the student’s ability.

The data were obtained from the Neuroscience courseware from January
to November 2021. Eight course pages where at least 500 students
engaged in the practice were examined using an item response
theory (IRT) approach to assess discrimination. We believe this data
set, containing 72,543 observations of student-question interactions
in natural learning contexts, to be the first of its kind for studying
discrimination of AG questions, useful for gaining insights into the
potential for AQG to enhance textbook content.

Page | Students | AG Questions | HA Questions | Total<br/>Responses
-----|----------|--------------|--------------|--------------------
4 | 583 | 9 | 10 | 9,465
11 | 855 | 8 | 11 | 14,048
13 | 598 | 3 | 10 | 7,181
14 | 561 | 2 | 12 | 7,437
23 | 668 | 1 | 9 | 6,189
24 | 568 | 12 | 13 | 12,650 
34 | 551 | 3 | 10 | 6,294
58 | 512 | 6 | 14 | 9,279

Further details can be found in the paper above.

## Data Files and Analyses

The Bayesian IRT code used to perform the analysis is not publicly
available, but the output of a Jupyter notebook of the analysis is
provided for each course page in the study, containing the IRT model
fit, convergence checks, and posterior predictive check.

The files provided are:

File | Description
-----|------------
responses_neuroscience_p4.txt | Response data for page 4 of the Neuroscience course
responses_neuroscience_p11.txt | Response data for page 11 of the Neuroscience course
responses_neuroscience_p13.txt | Response data for page 13 of the Neuroscience course
responses_neuroscience_p14.txt | Response data for page 14 of the Neuroscience course
responses_neuroscience_p23.txt | Response data for page 23 of the Neuroscience course
responses_neuroscience_p24.txt | Response data for page 24 of the Neuroscience course
responses_neuroscience_p34.txt | Response data for page 34 of the Neuroscience course
responses_neuroscience_p58.txt | Response data for page 58 of the Neuroscience course
[IRT Analysis Neuroscience Page 4.html](http://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/l%40s-2022/IRT%20Analysis%20Neuroscience%20Page%204.html) | IRT analysis for page 4 of the Neuroscience course
[IRT Analysis Neuroscience Page 11.html](http://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/l%40s-2022/IRT%20Analysis%20Neuroscience%20Page%2011.html) | IRT analysis for page 11 of the Neuroscience course
[IRT Analysis Neuroscience Page 13.html](http://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/l%40s-2022/IRT%20Analysis%20Neuroscience%20Page%2013.html) | IRT analysis for page 13 of the Neuroscience course
[IRT Analysis Neuroscience Page 14.html](http://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/l%40s-2022/IRT%20Analysis%20Neuroscience%20Page%2014.html) | IRT analysis for page 14 of the Neuroscience course
[IRT Analysis Neuroscience Page 23.html](http://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/l%40s-2022/IRT%20Analysis%20Neuroscience%20Page%2023.html) | IRT analysis for page 23 of the Neuroscience course
[IRT Analysis Neuroscience Page 24.html](http://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/l%40s-2022/IRT%20Analysis%20Neuroscience%20Page%2024.html) | IRT analysis for page 24 of the Neuroscience course
[IRT Analysis Neuroscience Page 34.html](http://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/l%40s-2022/IRT%20Analysis%20Neuroscience%20Page%2034.html) | IRT analysis for page 34 of the Neuroscience course
[IRT Analysis Neuroscience Page 58.html](http://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/l%40s-2022/IRT%20Analysis%20Neuroscience%20Page%2058.html) | IRT analysis for page 58 of the Neuroscience course
model_summary_neuroscience_p4.txt | IRT model summary from `pymc3` for page 4 of the Neuroscience course
model_summary_neuroscience_p11.txt | IRT model summary from `pymc3` for page 11 of the Neuroscience course
model_summary_neuroscience_p13.txt | IRT model summary from `pymc3` for page 13 of the Neuroscience course
model_summary_neuroscience_p14.txt | IRT model summary from `pymc3` for page 14 of the Neuroscience course
model_summary_neuroscience_p23.txt | IRT model summary from `pymc3` for page 23 of the Neuroscience course
model_summary_neuroscience_p24.txt | IRT model summary from `pymc3` for page 24 of the Neuroscience course
model_summary_neuroscience_p34.txt | IRT model summary from `pymc3` for page 34 of the Neuroscience course
model_summary_neuroscience_p.58txt | IRT model summary from `pymc3` for page 58 of the Neuroscience course

Data files are tab-delimited with one observation per line. The format
is the same as the difficulty data sets in our previous investigation
of AG question engagement, difficulty and persistence. The fields in
the data files are:

Field | Description
------|------------
`student` | Anonymized student identifier
`question` | Question identifier
`course_page_number` | Location of the question’s page within the course
`unit_page_number` | Location of the question’s page within its course unit
`module_page_number` | Location of the question’s page within its course module
`page_question_number` | Question’s number on its page
`question_type` | Identifier for question origin and format<br/>Examples:<br/>`AG_FITB` = automatically generated fill-in-the-blank<br/>`HA_MC` = human-authored multiple-choice
`answered` | Whether the student answered the question (always 1 here)
`correct` | Whether the student got the correct answer on the first attempt

## Contact Us

If you have questions, please feel free to email benny.johnson@vitalsource.com.
