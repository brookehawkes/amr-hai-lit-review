# Antimicrobial Resistance and Hospital Aquired Infections Topic Modeling from PubMed Abstracts

This project uses **Latent Dirichlet Allocation (LDA)** to identify major topics in PubMed abstracts related to *antimicrobial resistance (AMR)* and *hospital aquired infections*, spanning from 1990 to 2023. The goal is to visualize evolving themes in AMR-related research using unsupervised machine learning and natural language processing (NLP) techniques. Additionally, the goal is to see how these topics may have changed over time.

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



- Fetches all abstracts from PubMed using the `Bio.Entrez` API with the keywords "antimicrobial resistance AND hospital aquired infections"
- Cleans and preprocesses text using `nltk` and `spaCy`
- Performs topic modeling with **LDA** (`scikit-learn`)
- Visualizes topic trends over time with `plotly`
- Displays topic word clouds for easy interpretation

---

## Dataset




Project Overview: Briefly explain the task you're working on.

Dataset: Describe the dataset you're using (e.g., source, size, format).

Modeling Approach: Summarize the models you're using and why.

Installation Instructions: Guide for setting up the environment and installing dependencies.

How to Run the Code: Clear instructions for running each script.

Results: Brief description of what your results show.
