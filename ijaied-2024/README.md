# Evaluation of Automatically Generated Questions for Spanish Textbooks Dataset

This directory contains the supporting dataset and analysis code for
our project on evaluating the quality of automatically generated
questions for Spanish-language textbooks by subject matter experts
(SMEs). This research is discussed in our paper

Johnson, B. G., Van Campenhout, R., Jerome, B., Castro, M. F.,
Bistolfi, R., & Dittel, J. S. (2024). Automatic question generation
for Spanish textbooks: Evaluating Spanish questions generated with the
parallel construction method. *International Journal of Artificial
Intelligence in
Education*. [https://doi.org/10.1007/s40593-024-00394-1](https://doi.org/10.1007/s40593-024-00394-1)

This paper is part of a [Special Issue of IJAIED on Intelligent
Textbooks](https://link.springer.com/collections/jcjcecejaf).

## Description

The integration of formative practice questions with textbook content
is a well-known method for increasing student learning, and recent
advances in artificial intelligence have made automatic question
generation a viable option for scaling this learning method to
thousands of textbooks. To expand this method to even more students,
an approach called [parallel
construction](https://intextbooks.science.uu.nl/workshop2022/files/itb22_p5_short9847.pdf)
was developed to utilize the question generation process in English to
create questions for other languages, such as Spanish. However,
validation of the questions by native-speaking subject matter experts
is necessary to ensure the questions generated through parallel
construction are acceptable for educational purposes.

In this work, fill-in-the-blank (FITB) and matching cloze questions
were generated via parallel construction for Spanish-language
textbooks in six subjects: Accounting, Communication, Finance, Human
Resource Management, Marketing, and Psychology. The questions were
evaluated by faculty SMEs teaching those subjects at major
universities in Mexico and Argentina, with two reviewers per subject
except for Accounting, where only one reviewer was recruited.  The
results were compared to the research literature on evaluation of
automatically generated questions. Please see the paper above for the
details of the work.

## Data Files and Code Notebooks

The files provided are:

File | Description
-----|------------
question_reviews.xlsx | Question review dataset
Spanish Question Review Analysis.ipynb | Jupyter notebook for question review analysis
Question Review Instructions.docx | Instructions given to SME reviewers

The dataset is an Excel workbook with a separate worksheet for each
reviewer. Each worksheet tab is named using the textbook subject area
and reviewer number, e.g., `finance_reviewer_2`. The worksheet
columns are:

Column | Type | Definition
-------|------|-----------
`Rating` | categorical | Reviewer rating of question on five-point scale:<br>`1 Bad`, `2 Unacceptable`, `3 Borderline`, `4 Acceptable`, `5 Good`
`Reason` | categorical | Reason code for why question was rated 1, 2, or 3:<br/>`Ungrammaticality`, `Incorrect Information`, `Vagueness`, `Awkwardness`, `Other`
`Type` | categorical | Question type: `FITB`, `matching`
`Question` | string | Question stem
`Answer` | string | Correct answer word (`FITB`) or words (`matching`)
`Chapter` | string  | Title of textbook chapter from which question was generated
`Section` | string | Title of textbook section from which question was generated

The Jupyter notebook provided contains Python code for reproducing the
results given in the paper.

## Contact Us

If you have questions, please feel free to email benny.johnson@vitalsource.com.
