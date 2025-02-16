#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from nltk.corpus import stopwords
import pandas as pd

# Télécharger les stop words français
import nltk
nltk.download('stopwords')
french_stop_words = stopwords.words('french')

# Exemple de données
data = {
    'title': ['Film A', 'Film B', 'Film C', 'Film D'],
    'description': [
        'Un film d\'action avec des explosions et des courses-poursuites.',
        'Une comédie romantique pleine de moments drôles et touchants.',
        'Un thriller psychologique avec des rebondissements inattendus.',
        'Un film d\'aventure avec des voyages et des découvertes.'
    ]
}
# Convertir en DataFrame
df = pd.DataFrame(data)
print(df)


# In[2]:


# Vectorisation avec TF-IDF et stop words français
tfidf = TfidfVectorizer(stop_words=french_stop_words)
tfidf_matrix = tfidf.fit_transform(df['description'])

# Afficher la matrice TF-IDF
print(tfidf_matrix.shape)  # (nombre de films, nombre de mots uniques)
print(tfidf_matrix.toarray())  # Afficher la matrice dense


# In[23]:


# Calcul de la similarité cosinus entre les films
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Afficher la matrice de similarité
print(cosine_sim)


# In[25]:


def recommend_movies(title, cosine_sim, df):
    # Trouver l'index du film dans le DataFrame
    idx = df[df['title'] == title].index[0]
    
    # Obtenir les scores de similarité pour ce film
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Trier les films par score de similarité
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Exclure le film lui-même et prendre les 3 premiers
    sim_scores = sim_scores[1:4]
    
    # Obtenir les indices des films recommandés
    movie_indices = [i[0] for i in sim_scores]
    
    # Retourner les titres des films recommandés
    return df['title'].iloc[movie_indices]



# In[31]:


# Exemple : Recommander des films similaires à "Film A"
recommendations = recommend_movies('Film A',cosine_sim, df)
print(recommendations)


# In[ ]:




