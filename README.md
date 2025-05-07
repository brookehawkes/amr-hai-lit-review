# Antimicrobial Resistance and Hospital Aquired Infections Topic Modeling from PubMed Abstracts

This project uses **Latent Dirichlet Allocation (LDA)** to identify major topics in PubMed abstracts related to *antimicrobial resistance (AMR)* and *hospital aquired infections*, spanning from 2013 to 2024. The goal is to visualize evolving themes in AMR-related research using unsupervised machine learning and natural language processing (NLP) techniques. Additionally, the goal is to see how these topics may have changed over time.

---

## Project Overview

The project involves the following steps:

1. PubMed Abstract Retrieval: Abstracts related to "antimicrobial resistance AND hospital-acquired infection" are fetched using the PubMed E-utilities API.

2. Text Preprocessing: The fetched abstracts are preprocessed by removing stop words, punctuation, and performing lemmatization.

3. Topic Modeling: Latent Dirichlet Allocation (LDA) is used to extract topics from the preprocessed text data.

4. Visualization: Various visualizations are created, including:

    - Temporal trends of topic proportions over time.

    - Word clouds for each topic.

    - A word cloud showing the most common terms across all abstracts.

---

## Prerequisites
To run this project, you need to have Python installed, as well as the required libraries.

Python Libraries
The following libraries are required for the project:

- requests: For fetching data from PubMed API.

- nltk: For natural language processing tasks like stopword removal and lemmatization.

- spacy: For advanced text processing and tokenization.

- sklearn: For machine learning tasks like text vectorization and topic modeling.

- pandas: For data manipulation and storage.

- matplotlib, seaborn, plotly: For data visualization.

- wordcloud: For generating word clouds.

---

## Files
- processing_and_analysis.py: The main Python script to fetch, process, and analyze PubMed abstracts.

- requirements.txt: A list of Python dependencies required for the project.

- experiment.md: Detailed documentation of the experiment.

- results.md: Final results and analysis

