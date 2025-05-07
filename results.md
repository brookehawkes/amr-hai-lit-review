# Results: Topic Modeling on PubMed Abstracts

## Overview

This document presents the findings from applying Latent Dirichlet Allocation (LDA) to a collection of PubMed abstracts related to antimicrobial resistance and hospital-acquired infections. The analysis aimed to uncover latent topics within the literature and observe their trends over time.

## Key Findings

### Identified Topics

The LDA model extracted the following five topics:

1. **Topic 1: Urinary Tract Infections**
   - *Top Terms*: urinary, tract, urinary tract, risk, bacteria, factor, coli, mortality, risk factor, gramnegative

2. **Topic 2: Resistant Bacteria**
   - *Top Terms*: multidrugresistant, bacteria, methicillinresistant, pathogen, bacterial, organism, transmission, activity, healthcare, cell

3. **Topic 3: Associated Infections**
   - *Top Terms*: carbapenemresistant, hiv, cre, tuberculosis, difficile, enterobacteriaceae, tb, crab, pylorus, vancomycinresistant

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

### Word Frequencies by Topic

**Topic 1: Urinary Tract Infections**
![topic1_final](https://github.com/user-attachments/assets/9232c68e-9aeb-4018-ad9d-e67f53e6ee2b)

**Topic 2: Resistant Bacteria**
![topic2_final](https://github.com/user-attachments/assets/5d09ef78-35ec-46f3-b9f4-dc1a8d24571c)

**Topic 3: Associated Infections**
![topic3_final](https://github.com/user-attachments/assets/7ca9a7bb-b5f8-46d6-998f-65be52742670)

**Topic 4: Public Health Practices**
![topic4_final](https://github.com/user-attachments/assets/f690e682-9a98-4500-9001-455522df34b0)

**Topic 5: Biology of AMR**
![topic5_final](https://github.com/user-attachments/assets/ecdcc67e-8feb-4e48-86d0-e1a45ec43a82)

### Word Clouds

**Topic 1: Urinary Tract Infections**
![topic1_wordcloud](https://github.com/user-attachments/assets/29b5cbbc-e17f-472c-8894-69fd754ee54f)

**Topic 2: Resistant Bacteria**
![topic2_wordcloud](https://github.com/user-attachments/assets/cefbbdea-a145-4b83-b886-76c765070c04)

**Topic 3: Associated Infections**
![topic3_wordcloud](https://github.com/user-attachments/assets/e4cae91e-df33-4f89-9766-980a8f6c4553)

**Topic 4: Public Health Practices**
![topic4_wordcloud](https://github.com/user-attachments/assets/63f0f604-ce0a-470d-a8c9-d7b416162f6a)

**Topic 5: Biology of AMR**
![topic5_wordcloud](https://github.com/user-attachments/assets/0b9d1671-cc98-44a0-ab10-deec157d648b)

**Overall**
![overall_wordcloud](https://github.com/user-attachments/assets/acd02cbb-8d88-42d2-a1a8-deef9738b647)

## Interpretation

- The overall topics, and especially the increasing trend in **Topic 4**, underscores the increasing focus on public health and preventative measures for AMR in hospital settings.

## Potential Future Work

- Expand the dataset to include full-text articles for a more comprehensive analysis.
- Incorporate additional metadata (e.g., geographic location, journal impact factor) to enrich the analysis.

