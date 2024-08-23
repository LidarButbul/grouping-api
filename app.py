#!/usr/bin/env python
# coding: utf-8

from fastapi import FastAPI
from pydantic import BaseModel
import torch
from transformers import BertTokenizer, BertModel
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import nest_asyncio
import uvicorn
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

app = FastAPI()
nest_asyncio.apply()

import nltk
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()


class ClaimsRequest(BaseModel):
    claims: list
    n_clusters: int


def remove_stopwords(claim):
    words = word_tokenize(claim)
    cleaned_claim = ' '.join([word for word in words if word.lower() not in stop_words])
    return cleaned_claim

# stemming
def preprocess_claim(claim):
    words = word_tokenize(claim)
    final_claims = ' '.join([stemmer.stem(word) for word in words if word.lower() not in stop_words])
    return final_claims

def group_claims(claims, n_clusters):
    # Preprocessing
    cleaned_claims = [remove_stopwords(claim) for claim in claims]
    final_claims = [preprocess_claim(claim) for claim in cleaned_claims]
    
    model = SentenceTransformer('all-MiniLM-L6-v2')  # מודל SBERT קטן אך יעיל
    embeddings = model.encode(final_claims)


    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(embeddings)
    labels = kmeans.labels_

    # Clustering
    clusters = {}
    for label, claim in zip(labels, claims):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(claim)
    
    # Generate topics with LDA 
    vectorizer = CountVectorizer(stop_words='english')
    lda = LatentDirichletAllocation(n_components=1, random_state=42)
    
    topics = []
    for cluster_id, cluster_claims in clusters.items():
        if len(cluster_claims) > 0:
            X = vectorizer.fit_transform(cluster_claims)
            lda.fit(X)
            words = vectorizer.get_feature_names_out()
            topic_words = [words[i] for i in lda.components_[0].argsort()[-2:]]  # 2 words for topics
            topics.append({
                'title': " ".join(topic_words),
                'number_of_claims': len(cluster_claims)
            })
    
    return topics

@app.post('/group')
async def group_endpoint(request: ClaimsRequest):
    topics = group_claims(request.claims, request.n_clusters)
    return {"groups": topics}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Claim Grouping API!"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


# In[ ]:




