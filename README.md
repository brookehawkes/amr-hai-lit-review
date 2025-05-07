# Antimicrobial Resistance and Hospital Aquired Infections Topic Modeling from PubMed Abstracts

This project uses **Latent Dirichlet Allocation (LDA)** to identify major topics in PubMed abstracts related to *antimicrobial resistance (AMR)* and *hospital aquired infections*, spanning from 1990 to 2023. The goal is to visualize evolving themes in AMR-related research using unsupervised machine learning and natural language processing (NLP) techniques. Additionally, the goal is to see how these topics may have changed over time.

---

## Features

- Fetches all abstracts from PubMed using the `Bio.Entrez` API with the keywords "antimicrobial resistance AND hospital aquired infections"
- Cleans and preprocesses text using `nltk` and `spaCy`
- Performs topic modeling with **LDA** (`scikit-learn`)
- Visualizes topic trends over time with `plotly`
- Displays topic word clouds for easy interpretation

---

## Project Setup
