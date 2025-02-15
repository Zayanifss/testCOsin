# Image de base Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .

COPY test1.py .  

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt && \
    python -m nltk.downloader stopwords  # Télécharger les stopwords NLTK

# Commande d'exécution
CMD ["python", "./test1.py"]