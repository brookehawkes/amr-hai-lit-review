# Results: Topic Modeling on PubMed Abstracts

## Overview

This document presents the findings from applying Latent Dirichlet Allocation (LDA) to a collection of PubMed abstracts related to antimicrobial resistance and hospital-acquired infections. The analysis aimed to uncover latent topics within the literature and observe their trends over time.

## Key Findings

### Identified Topics

The LDA model extracted the following five topics:

1. **Topic 1: Urinary Tract Infections**
   - *Top Terms*: urinary, tract, urinary tract, risk, bacteria

2. **Topic 2: Resistant Bacteria**
   - *Top Terms*: multidrugresistant, bacteria, methicillinresistant, pathogen, bacterial

3. **Topic 3: Associated Infections**
   - *Top Terms*: carbapenemresistant, hiv, cre, tuberculosis, difficile, enterobacteriaceae

4. **Topic 4: Public Health Practices**
   - *Top Terms*: health, use, stewardship, HAIs, covid, country, public, global, public helath, practice

5. **Topic 5: Biology of AMR**
   - *Top Terms*: isolates, strain, baumannii, gene, mrsa, aureus, penumoniae, staphylococcus, acinetobacter, nosocomial

### Temporal Trends

Analysis of topic prevalence over publication years revealed:

- **Topic 2** (Resistant Bacteria) and **Topic 4** (Public Health Practices) showed a steady increase from 2012 to 2024, indicating potentially more public health and prevention efforts in regards to AMR.
- **Topic 1** (Urinary Tract Infections) and **Topic 5** (Biology of AMR) have steadily decreased since 2012, potentially due to more research efforts being focused elsewhere.
- **Topic 3** (Associated Infections) has remained steady over time.

## Visualizations

### Topic Distribution Over Time

<img width="1890" alt="amr_overtime" src="https://github.com/user-attachments/assets/ef2d12ef-c0a4-4372-9112-b6289e5376f7" />

*Figure 1: Proportion of each topic across publication years.*

### Word Clouds

**Topic 1: Infection Control Measures**

![Topic 1 Word Cloud](images/topic1_wordcloud.png)

**Topic 2: Antibiotic Resistance Mechanisms**

![Topic 2 Word Cloud](images/topic2_wordcloud.png)

*... (Include word clouds for remaining topics similarly)*

## Interpretation

- The increasing trend in **Topic 2** underscores the escalating concern over antibiotic resistance mechanisms in clinical settings.
- The prominence of **Topic 5** in recent years reflects the emphasis on developing and implementing rapid diagnostic methods to curb hospital-acquired infections.

## Future Work

- Expand the dataset to include full-text articles for a more comprehensive analysis.
- Experiment with different numbers of topics to optimize model granularity.
- Incorporate additional metadata (e.g., geographic location, journal impact factor) to enrich the analysis.

