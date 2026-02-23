# Concevez_et_deployez_un_systeme_RAG
## Présentation du projet

PulsEvent est une solution de **RAG (Retrieval-Augmented Generation)** permettant d'interroger intelligemment une base de données massive de **2 Go** d'événements culturels (issus d'OpenAgenda).

Grâce à l'IA, le système comprend les questions complexes des utilisateurs et extrait les informations pertinentes de la base de données pour générer une réponse précise et naturelle, évitant ainsi les "hallucinations" classiques des modèles de langage.

---

##  Objectifs & Compétences

Ce projet valide les étapes clés d'un pipeline de données IA :

- **Nettoyage de données massives** : Filtrage et traitement de gros fichiers JSON.
- **Recherche Sémantique** : Mise en place d'un index vectoriel pour retrouver des événements par contexte.
- **Qualité logicielle** : Utilisation de tests unitaires et de docstrings pour un code maintenable.

---

##  Architecture Technique

Le système repose sur une chaîne technique moderne :

- **LLM** : Mistral AI (modèle de langage français performant).
- **Orchestrateur** : LangChain (pour lier les données et l'IA).
- **Base Vectorielle** : FAISS (Facebook AI Similarity Search) pour la rapidité de recherche.
- **Python 3.10+** : Langage principal du projet.

---

##  Structure des fichiers

---

##  Instructions de déploiement

### 1. Installation de l'environnement

Clonez le dépôt et installez les bibliothèques nécessaires :

### 2. Configuration de l'API

Créez un fichier `.env` à la racine du projet et insérez votre clé :

### 3. Lancement du pipeline

Suivez les étapes dans l'ordre pour préparer les données :

1. **Pré-processing** : `python scripts/pre_processing.py`
2. **Vectorisation** : `python scripts/vectorisation.py`
3. **Lancer l'assistant** : `python scripts/app.py`

---

##  Tests Unitaires & Qualité

Pour garantir la fiabilité du nettoyage des données, un pipeline de tests est intégré. Lancez-le avec la commande :

*Toutes les fonctions sont documentées via des **docstrings** respectant les standards Python.*


