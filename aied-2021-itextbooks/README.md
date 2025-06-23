# Transforming Textbooks into Learning by Doing Environments Dataset

This directory contains the dataset and analysis code supporting our
research on transforming textbooks into interactive learning
environments using automatic question generation. This work is
detailed in the following publication:

Van Campenhout, R., Dittel, J. S., Jerome, B., & Johnson,
B. G. (2021). Transforming textbooks into learning by doing
environments: An evaluation of textbook-based automatic question
generation. In *Proceedings of the Third Workshop on Intelligent
Textbooks at the 22nd International Conference on Artificial
Intelligence in Education* (pp. 60–73). CEUR Workshop
Proceedings. [http://ceur-ws.org/Vol-2895/paper06.pdf](http://ceur-ws.org/Vol-2895/paper06.pdf)

The paper was presented in the [Third Workshop on Intelligent
Textbooks
(iTextbooks)](https://intextbooks.science.uu.nl/workshop2021/), part
of the [22nd Annual Conference on Artificial Intelligence in
Education](https://aied2021.science.uu.nl/).

## Description

Integrating formative practice questions with textbook content has
been shown to significantly enhance student learning. However, the
creation of these questions is labor-intensive and costly. Automatic
question generation (AQG) offers a promising solution to scale
formative practice efficiently.

This dataset supports our large-scale evaluation of textbook-based AQG
across six college courses, where automatically generated (AG)
questions were used alongside human-authored (HA)
questions. Performance metrics include engagement, difficulty, and
persistence, capturing how students interacted with these formative
questions.

| Course          | Students | AG Questions | HA Questions | Engagement Observations | Difficulty Observations | Persistence Observations |
| --------------- | -------- | ------------ | ------------ | ----------------------- | ----------------------- | ------------------------ |
| Neuroscience    | 516      | 747          | 888          | 286,129                 | 120,098                 | 34,124                   |
| Communication A | 109      | 263          | 390          | 43,538                  | 20,990                  | 5,643                    |
| Microbiology    | 99       | 416          | 690          | 71,119                  | 42,114                  | 10,520                   |
| Psychology      | 91       | 607          | 48           | 34,757                  | 29,583                  | 4,926                    |
| Communication B | 79       | 386          | 533          | 35,351                  | 17,547                  | 4,806                    |
| Accounting      | 51       | 191          | 403          | 14,661                  | 8,309                   | 2,027                    |

## Data Files and Code Notebooks

This directory provides a comprehensive set of detailed regression
analyses for each course and metric that could not be included in the
paper due to the page limit:

| File                                                                                                                                                                     | Description                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- |
| [persistence_trends.pdf](https://github.com/vitalsource/data/blob/main/aied-2021-itextbooks/persistence_trends.pdf)                                                      | Persistence trends across all courses                 |
| [engagement_neuroscience.html](https://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/aied-2021-itextbooks/engagement_neuroscience.html)           | Engagement regression analysis for Neuroscience       |
| [engagement_communication_a.html](https://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/aied-2021-itextbooks/engagement_communication_a.html)     | Engagement regression analysis for Communication A    |
| [engagement_microbiology.html](https://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/aied-2021-itextbooks/engagement_microbiology.html)           | Engagement regression analysis for Microbiology       |
| [engagement_psychology.html](https://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/aied-2021-itextbooks/engagement_psychology.html)               | Engagement regression analysis for Psychology         |
| [engagement_communication_b.html](https://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/aied-2021-itextbooks/engagement_communication_b.html)     | Engagement regression analysis for Communication B    |
| [engagement_accounting.html](https://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/aied-2021-itextbooks/engagement_accounting.html)               | Engagement regression analysis for Accounting         |
| [difficulty_neuroscience.html](https://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/aied-2021-itextbooks/difficulty_neuroscience.html)           | Difficulty regression analysis for Neuroscience       |
| [difficulty_communication_a.html](https://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/aied-2021-itextbooks/difficulty_communication_a.html)     | Difficulty regression analysis for Communication A    |
| [difficulty_microbiology.html](https://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/aied-2021-itextbooks/difficulty_microbiology.html)           | Difficulty regression analysis for Microbiology       |
| [difficulty_psychology.html](https://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/aied-2021-itextbooks/difficulty_psychology.html)               | Difficulty regression analysis for Psychology         |
| [difficulty_communication_b.html](https://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/aied-2021-itextbooks/difficulty_communication_b.html)     | Difficulty regression analysis for Communication B    |
| [difficulty_accounting.html](https://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/aied-2021-itextbooks/difficulty_accounting.html)               | Difficulty regression analysis for Accounting         |
| [persistence_neuroscience.html](https://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/aied-2021-itextbooks/persistence_neuroscience.html)         | Persistence regression analysis for Neuroscience      |
| [persistence_communication_a.html](https://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/aied-2021-itextbooks/persistence_communication_a.html)   | Persistence regression analysis for Communication A   |
| [persistence_microbiology.html](https://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/aied-2021-itextbooks/persistence_microbiology.html)         | Persistence regression analysis for Microbiology      |
| [persistence_psychology.html](https://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/aied-2021-itextbooks/persistence_psychology.html)               | Persistence regression analysis for Psychology      |
| [persistence_communication_b.html](https://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/aied-2021-itextbooks/persistence_communication_b.html)     | Persistence regression analysis for Communication B |
| [persistence_accounting.html](https://htmlpreview.github.io/?https://github.com/vitalsource/data/blob/main/aied-2021-itextbooks/persistence_accounting.html)               | Persistence regression analysis for Accounting      |

## Contact Us

If you have questions, please feel free to email
[benny.johnson@vitalsource.com](mailto:benny.johnson@vitalsource.com).

