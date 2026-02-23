## Présentation du Projet

PulsEvent est une solution de **RAG (Retrieval-Augmented Generation)** conçue pour transformer une base de données brute et massive (**2 Go de données JSON** issues d'OpenAgenda) en un assistant conversationnel fluide.

Contrairement à un chatbot classique, PulsEvent n'invente rien : il va chercher l'information réelle dans les fichiers vectorisés avant de répondre, garantissant ainsi une fiabilité totale des informations (dates, lieux, tarifs des événements parisiens).

---

##  Objectifs & Compétences Validées

Ce projet démontre la maîtrise d'un pipeline complet d'ingénierie IA :

1. **Ingénierie de la Donnée (Data Engineering)** :
    - Parsing et filtrage d'un dataset de 2 Go.
    - Gestion de la mémoire vive lors de la lecture des fichiers JSON.
2. **Architecture RAG & Vectorisation** :
    - Mise en œuvre d'embeddings via Mistral AI.
    - Stockage et indexation haute performance avec **FAISS**.
3. **Qualité et Fiabilité (QA)** :
    - Développement de tests unitaires avec `pytest`.
    - Documentation technique exhaustive (Docstrings Google Style).

---

##  Architecture Technique & Choix Technologiques

Le système repose sur une "stack" moderne choisie pour sa rapidité et sa compatibilité :

- **Modèle de Langage (LLM)** : `Mistral-7B` (via API Mistral). Choisi pour sa performance exceptionnelle en langue française.
- **Orchestrateur** : `LangChain`. Utiliser LangChain permet de créer des chaînes de décision (Chains) qui gèrent automatiquement la mémoire de la conversation.
- **Base Vectorielle** : `FAISS`. Préférée à une base cloud pour ce POC pour sa rapidité de recherche en local (recherche par similarité cosinus).
- **Environnement** : `Python 3.10+` avec gestion des variables d'environnement via `python-dotenv`.

---

##  Structure Détaillée des Fichiers

---

##  Instructions de Déploiement

### 1. Installation de l'environnement

Clonez le dépôt et créez un environnement virtuel pour isoler les dépendances :

### 2. Configuration de l'API

Le projet nécessite une clé API Mistral. Créez un fichier `.env` à la racine :

### 3. Cycle de vie de la donnée

Le projet suit un flux précis :

1. **Pré-processing** : `python scripts/pre_processing.py`
    - Réduit le fichier de 2 Go en un fichier exploitable de quelques Mo.
2. **Vectorisation** : `python scripts/vectorisation.py`
    - Découpe les événements en "chunks" et les transforme en vecteurs numériques.
3. **Lancement** : `python scripts/app.py`
    - Démarre la session de chat.

---

##  Tests Unitaires & Qualité

La fiabilité du système est vérifiée à chaque modification majeure :

- **Pipeline de Tests** : `pytest tests/test_pipeline.py`
- **Couverture** : Nettoyage de texte, validation de format de date, et intégrité des données filtrées.
- **Documentation** : Toutes les fonctions utilisent des docstrings détaillant les types d'entrée (`Args`) et de sortie (`Returns`).
