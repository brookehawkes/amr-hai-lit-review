# Results: Topic Modeling on PubMed Abstracts

## Overview

This document presents the findings from applying Latent Dirichlet Allocation (LDA) to a collection of PubMed abstracts related to antimicrobial resistance and hospital-acquired infections. The analysis aimed to uncover latent topics within the literature and observe their trends over time.

## Key Findings

### Identified Topics

The LDA model extracted the following five topics:

1. **Topic 1: Infection Control Measures**
   - *Top Terms*: hand hygiene, isolation, compliance, protocol, prevention

2. **Topic 2: Antibiotic Resistance Mechanisms**
   - *Top Terms*: resistance genes, plasmids, mutation, efflux pumps, gene transfer

3. **Topic 3: Clinical Treatment Strategies**
   - *Top Terms*: antibiotic therapy, dosage, treatment outcomes, patient response, clinical trials

4. **Topic 4: Hospital-Acquired Infection Epidemiology**
   - *Top Terms*: incidence rates, outbreak, surveillance, nosocomial infections, risk factors

5. **Topic 5: Diagnostic and Screening Techniques**
   - *Top Terms*: PCR, culture methods, sensitivity, specificity, rapid tests

### Temporal Trends

Analysis of topic prevalence over publication years revealed:

- **Topic 2** (Antibiotic Resistance Mechanisms) showed a steady increase from 2010 to 2020, indicating growing research interest.
- **Topic 4** (Hospital-Acquired Infection Epidemiology) peaked around 2015, possibly due to heightened awareness and reporting.
- **Topic 5** (Diagnostic and Screening Techniques) saw a surge post-2018, aligning with advancements in rapid diagnostic tools.

## Visualizations

### Topic Distribution Over Time

![Topic Distribution Over Time](images/topic_distribution_over_time.png)

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

## Limitations

- The dataset was limited to abstracts, which may not capture the full depth of research articles.
- The selection of five topics was arbitrary; exploring different numbers could yield alternative insights.
- Temporal analysis is constrained by the publication dates of available abstracts, which may not represent real-time research developments.

## Future Work

- Expand the dataset to include full-text articles for a more comprehensive analysis.
- Experiment with different numbers of topics to optimize model granularity.
- Incorporate additional metadata (e.g., geographic location, journal impact factor) to enrich the analysis.

