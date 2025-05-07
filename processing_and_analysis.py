import requests
import time
from xml.etree import ElementTree
import spacy
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation as LDA
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
from wordcloud import WordCloud
from collections import Counter
from sklearn.decomposition import LatentDirichletAllocation


# Initialize spaCy and NLTK components
nltk.download('stopwords')
nltk.download('wordnet')
nlp = spacy.load('en_core_web_sm')
lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words('english'))

# Define custom stopwords to ignore

custom_stopwords = {
    'disease', 'diseases', 'disorders', 'diseased',
    'disorder', 'syndrome', 'patient', 'patients', 'clinical',
    'expression', 'treated', 'treatment', 'associated', 'including',
    'study', 'studies', 'conclusion', 'result', 'results', 'objective',
    'group', 'groups', 'levels', 'significantly', 'investigated',
    'observed', 'indicated', 'shown', 'suggests', 'based', 'data',
    'method', 'methods', 'model', 'models', 'background', 'analysis',
    'findings', 'aim', 'purpose', 'among', 'used', 'identified',
    'may', 'can', 'could', 'would', 'also', 'well', 'one', 'two',
    'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
    'amyotrophic', 'lateral', 'sclerosis', 'als', 'case', 'using',
    'abstract', 'aimed', 'aims', 'people', 'investigate', 'investigated',
    'association', 'function', 'functions', 'measure', 'survival', 
    'phenotype', 'score', 'used', 'care', 'control', 'progressing', 
    'challenging', 'predictor', 'neurodegenerative', 'progression', 
    'clinical', 'role', 'user', 'potential', 'therapy', 'however',
    'review', 'repeat', 'whether', 'determine', 'event', 'measure',
    'corrects', 'articles', 'doi', 'reading', 'research', 'national',
    'since', 'report', 'synthesized', 'conducted', 'retrospective', 
    'prospective', 'antimicrobial', 'antibiotic', 'resistance', 'amr',
    'drug', 'caused', 'contact', 'mdr', 'systematic', 'assess', 'prevalence',
    'recommendation', 'due', 'characterize', 'contribute', 'highlight', 'analyze',
    'previously', 'conventional', 'administration', 'infection', 'hospital', 'infections'
}

# Combine
my_stop_words = list(stop_words.union(custom_stopwords))

# Update the preprocess_text function to exclude custom stopwords
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    doc = nlp(text)
    words = [token.text for token in doc if token.is_alpha]
    words = [word for word in words if word not in stop_words]
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)

# PubMed abstract retrieval
def fetch_pubmed_abstracts():
    # Extract PubMed abstracts
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    search_params = {
        "db": "pubmed",
        "term": "antimicrobial resistance AND hospital-acquired infection",
        "usehistory": "y",       
        "retmax": 0,             
        "retmode": "xml"
    }

    search_response = requests.get(search_url, params=search_params)
    search_root = ElementTree.fromstring(search_response.text)

    # Extract WebEnv, QueryKey, and total count
    webenv = search_root.findtext(".//WebEnv")
    query_key = search_root.findtext(".//QueryKey")
    total_count = int(search_root.findtext(".//Count"))

    print(f"Found {total_count} articles. Fetching in chunks...")

    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    retmax = 100  # how many articles to fetch per request
    results = []

    # Fetch abstracts in chunks
    for retstart in range(0, total_count, retmax):  
        print(f"Fetching articles {retstart + 1} to {retstart + retmax}...")

        fetch_params = {
            "db": "pubmed",
            "WebEnv": webenv,
            "query_key": query_key,
            "retstart": retstart,
            "retmax": retmax,
            "retmode": "xml"
        }

        fetch_response = requests.get(fetch_url, params=fetch_params)
        fetch_root = ElementTree.fromstring(fetch_response.text)

        # Extract titles + abstracts
        for article in fetch_root.findall(".//PubmedArticle"):
            title_elem = article.find(".//ArticleTitle")
            abstract_elem = article.find(".//Abstract/AbstractText")
            pubdate_elem = article.find(".//PubDate/Year")

            title = title_elem.text if title_elem is not None else "No title"
            abstract = abstract_elem.text if abstract_elem is not None else "No abstract"
            if pubdate_elem is not None and pubdate_elem.text is not None:
                pubdate = pubdate_elem.text
            results.append((title, abstract, pubdate))

        time.sleep(0.34)  

    return results

# Main execution
if __name__ == "__main__":
    # Fetch abstracts
    pubmed_abstracts = fetch_pubmed_abstracts()

    # Filter out articles with missing abstract or year
    cleaned_pubmed_abstracts = [
        (abstract, pubdate) for _, abstract, pubdate in pubmed_abstracts
        if abstract is not None and pubdate is not None
    ]

    # Preprocess each abstract
    processed_abstracts = [preprocess_text(abstract) for abstract, _ in cleaned_pubmed_abstracts]
    years = [pubdate for _, pubdate in cleaned_pubmed_abstracts]

    df = pd.DataFrame({
        'year': years,
        'abstract': processed_abstracts
    })


    # Vectorize the processed abstracts
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=5000, stop_words=my_stop_words)
    X = vectorizer.fit_transform(df['abstract'])

    # Perform Topic Modeling using LDA (Latent Dirichlet Allocation)
    lda_model = LatentDirichletAllocation(
        n_components=5, 
        doc_topic_prior=0.1,      
        topic_word_prior=0.05,    
        random_state=27
    )  
    lda_topics = lda_model.fit_transform(X)

    # Display topics
    terms = vectorizer.get_feature_names_out()
    for topic_idx, topic in enumerate(lda_model.components_):
        print(f"Topic {topic_idx + 1}:")
        print(" ".join([terms[i] for i in topic.argsort()[:-10 - 1:-1]]))
        print("\n")

    # Track Topic Proportions Over Time
    topic_proportions = lda_topics / lda_topics.sum(axis=1, keepdims=True)
    df_topics = pd.DataFrame(topic_proportions, columns=[f"Topic {i+1}" for i in range(lda_model.n_components)])
    df_topics['year'] = df['year']

    # Group by year and compute the average topic proportions
    topic_proportions_by_year = df_topics.groupby('year').mean().reset_index()
    topic_proportions_by_year_smooth = topic_proportions_by_year.rolling(window=3).mean()

    # Visualize the temporal trends of topics over the years
    fig = px.line(topic_proportions_by_year_smooth, x='year', y=[f"Topic {i+1}" for i in range(lda_model.n_components)],
                  labels={"value": "Topic Proportion", "variable": "Topic"},
                  title="Topic Proportions Over Time")
    fig.update_layout(xaxis_title="Year", yaxis_title="Proportion")
    fig.show()

    # Enhanced Topic Visualization with Seaborn (Top 10 words for each topic)
    n_top_words = 10
    for topic_idx, topic in enumerate(lda_model.components_):
        plt.figure(figsize=(10, 5))
        top_words_idx = topic.argsort()[:-n_top_words - 1:-1]
        top_words = [terms[i] for i in top_words_idx]
        top_weights = topic[top_words_idx]
        
        sns.barplot(x=top_weights, y=top_words, palette="Blues_d")
        plt.title(f"Top Words for Topic {topic_idx + 1}")
        plt.xlabel("Word Importance")
        plt.ylabel("Words")
        plt.show()

# Generate word clouds for each topic
for topic_idx, topic in enumerate(lda_model.components_):
    top_words_idx = topic.argsort()[:-30 - 1:-1] 
    top_words = [terms[i] for i in top_words_idx]
    top_weights = topic[top_words_idx]
    
    word_freq = {terms[i]: topic[i] for i in top_words_idx}

    wordcloud = WordCloud(width=800, height=400, background_color='white',
                          colormap='tab10').generate_from_frequencies(word_freq)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"Word Cloud for Topic {topic_idx + 1}")
    plt.show()

all_words = " ".join(df['abstract']).split()
word_counts = Counter(all_words)

wordcloud = WordCloud(width=1000, height=500, background_color='white',
                      colormap='viridis').generate_from_frequencies(word_counts)

plt.figure(figsize=(15, 7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of All Abstracts")
plt.show()


