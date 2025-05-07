# Experiment Report: Topic Modeling on PubMed Abstracts

## Objective

The primary objective of this project is to apply unsupervised learning techniques, specifically Latent Dirichlet Allocation (LDA), to a collection of PubMed abstracts related to **antimicrobial resistance** and **hospital-acquired infections**. The goal is to discover latent topics discussed in the literature and analyze their prevalence over time.

## Research Question

- **Main Question**: What are the dominant topics in research literature discussing antimicrobial resistance and hospital-acquired infections, and how have these topics evolved over time?

## Data Collection

### Source

- **Database**: PubMed (via Entrez API)
- **Query**: `"antimicrobial resistance" AND "hospital-acquired infection"`
- **Fields Used**: 
  - Title
  - Abstract
  - Publication Date (used to group topics over time)

### Retrieval Method

- Used the Entrez `esearch` and `efetch` utilities to retrieve abstracts.
- Filtered out records with missing or incomplete abstract fields.

## Preprocessing

Text preprocessing included the following steps:

1. **Lowercasing**: Converted all text to lowercase.
2. **Tokenization**: Used SpaCy to tokenize the text into words.
3. **Stopword Removal**: Removed common English stopwords using `nltk.corpus.stopwords`.
4. **Lemmatization**: Reduced each token to its base form using SpaCy’s lemmatizer.
5. **Filtering**:
   - Removed tokens that are not alphabetic.
   - Removed short tokens (length ≤ 3).

The cleaned tokens were then joined back into a single string per abstract for vectorization.

## Modeling

### Technique Used

- **Model**: Latent Dirichlet Allocation (LDA)
- **Library**: `sklearn.decomposition.LatentDirichletAllocation`

### Parameters

- `n_components` (number of topics): 5 (chosen based on interpretability)
- `max_iter`: 10
- `learning_method`: `'online'`
- `random_state`: 42

### Vectorization

- Used `CountVectorizer` from `sklearn` with:
  - `min_df=5` (terms must appear in at least 5 documents)
  - `max_df=0.9` (terms appearing in >90% of docs are excluded)
  - `stop_words='english'`

## Evaluation

### Topic Interpretability

- Manually inspected the top 10 words per topic to assign rough thematic labels (e.g., **infection control**, **drug resistance**, **clinical treatment**).
- Example top words for one topic: mrsa, pneumonia, methicillinresistant, aureus, unit, intensive, intensive unit, multidrugresistant, icu, mortality

### Temporal Analysis

- Aggregated topic proportions per abstract and grouped by year of publication.
- Visualized the change in topic proportions over time using line plots.

## Visualizations

1. **Topic Proportions Over Time**: Showed the percentage of documents dominated by each topic per year.
2. **Topic Word Clouds**: Generated word clouds for each topic using the most influential terms.
3. **Overall Word Cloud**: A word cloud of all terms in the corpus to illustrate frequent terms across the dataset.

## Key Findings

- **Shifts Over Time**: Topics related to antimicrobial stewardship rose steadily after the past few years, possibly related to initiatives related to appropriate antibiotic use and decreased prescribing.
- **Topic Diversity**: Some abstracts span multiple topics, reflecting interdisciplinary approaches in the field.
- **Recurrent Themes**: Resistance genes, treatment outcomes, and hospital interventions are consistently prominent.

## Limitations

- The number of topics (5) was selected heuristically; further tuning or coherence-based selection could improve results.
- Abstracts do not contain the full context of articles; results might differ using full-text analysis.

## Conclusion

This experiment demonstrates that LDA can effectively uncover thematic structures in PubMed literature on antimicrobial resistance and hospital-acquired infections. The visualizations provide insight into the evolution of research focus over time and may help inform future investigations in this domain.

