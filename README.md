# Analyse de Sentiments des Avis TripAdvisor

## Présentation du projet

Ce projet vise à concevoir et déployer une solution complète d’analyse de sentiments appliquée aux avis clients issus de la plateforme **TripAdvisor**, dans le contexte du tourisme (visites guidées).

L’objectif est d’aller au-delà des simples notes (étoiles) afin de mieux comprendre le **ressenti réel exprimé dans les commentaires textuels**, en tenant compte des nuances linguistiques. Le projet couvre l’ensemble du pipeline data : **collecte, traitement, modélisation, évaluation et restitution des résultats via une application interactive**.

---

## Problématique

Les notes attribuées par les utilisateurs ne reflètent pas toujours fidèlement le sentiment exprimé dans le texte (ironie, exagération, contradictions).

**Problématique centrale :**

> Comment mettre en place une solution d’analyse de sentiments robuste et fiable, capable de capturer les nuances linguistiques des avis clients et de fournir des insights actionnables pour l’amélioration des services touristiques ?

---

## Données

* **Source** : Web scraping de la plateforme TripAdvisor
* **Type de données** : Avis textuels + notes (1 à 5 étoiles)
* **Nombre d’avis** : 657
* **Période couverte** :  Novembre 2025
* **Langue** : Français

Les données présentent un **biais positif**, typique des plateformes d’avis, justifiant l’usage de techniques NLP avancées.

---

## Méthodologie

### 1. Collecte des données

* Web scraping des avis clients (texte, note, date)
* Constitution d’un jeu de données exploitable pour l’analyse

### 2. Prétraitement des textes

* Passage en minuscules
* Suppression des URLs, ponctuations et caractères spéciaux
* Normalisation des espaces
* Préparation des textes pour les modèles NLP

### 3. Analyse de sentiments

Plusieurs approches ont été implémentées et comparées :

**Approches lexicales**

* VADER
* TextBlob

**Approches Machine Learning**

* Naïve Bayes (TF-IDF)

**Approche avancée (Deep Learning)**

* Modèle Transformer spécialisé pour les commentaires touristiques (Hugging Face)

### 4. Évaluation des modèles

Les prédictions ont été comparées aux notes réelles normalisées à l’aide de :

* Corrélation de Pearson
* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)

### 5. Extraction d’insights

* Extraction de mots-clés via TF-IDF
* Analyse thématique globale
* Analyse différenciée par sentiment (positif / négatif)

---

## Résultats clés

* Les modèles **Machine Learning** et **Transformers** surpassent largement les approches lexicales
* Le modèle **Naïve Bayes** obtient les meilleures performances globales
* Les mots-clés révèlent que la **qualité du guide** est l’élément le plus déterminant (et polarisant)
* Identification de points d’amélioration logistiques (billets, organisation, éclairage, transport)

---

## Application Streamlit

Une application interactive a été développée pour :

* Visualiser la distribution des sentiments
* Explorer les résultats par avis
* Tester l’analyse de sentiments en temps réel

🔗 **Lien vers l’application Streamlit** :
[https://out7ier-sentiment-analysis.streamlit.app/](https://out7ier-sentiment-analysis.streamlit.app/)

---

## Stack technique

* **Langage** : Python
* **Manipulation de données** : Pandas, NumPy
* **Web scraping** : BeautifulSoup / Selenium
* **NLP** : NLTK, VADER, TextBlob
* **Machine Learning** : Scikit-learn (TF-IDF, Naïve Bayes)
* **Deep Learning / NLP avancé** : Transformers (Hugging Face)
* **Visualisation & déploiement** : Streamlit

---

## Cadre du projet

* **Type** : Projet académique
* **Réalisation** : Travail en équipe
* **Contribution personnelle** :

  * Web scraping des données
  * Prétraitement et modélisation NLP
  * Analyse comparative des modèles
  * Développement de l’application Streamlit

---

## Perspectives

* Enrichissement du jeu de données
* Fine-tuning de modèles Transformers
* Détection du sarcasme et des émotions
* Mise en production à plus grande échelle

---

## Auteurs

DJEDJE EMMANUEL LEVY ,
FOFANA WAKOU SOULEYMANE JASON ,
YAKE CHRISTELLE REBECCA
