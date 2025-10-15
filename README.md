

---

**Projet TP – ETL : Analyse des écarts de salaires à Boston**

**Auteurs :**

* Gloire BOUNGOU (Responsable du repo GitHub)
* Valence OKO
* Ann-Jireh MVOUTOU
* LIBIZANGOMO LOUMA
* Arcy MIAMBANZILA

**Encadrant :** Antoine Lucsko
**Date :** 15 octobre 2025
**Cours :** DataOps 

---

### 1. Contexte

L’objectif de ce projet est de mettre en œuvre un pipeline ETL complet (Extract, Transform, Load) pour analyser les écarts de salaires des employés municipaux de la ville de Boston sur l’année 2018.

Objectifs principaux :

* Extraire les données depuis une API publique.
* Nettoyer et transformer ces données pour les rendre exploitables.
* Charger les données dans un fichier CSV propre.
* Réaliser une analyse statistique par département (min, max, moyenne, médiane, effectif).

Source des données :
City of Boston Payroll Data (API)
[https://data.boston.gov/api/3/action/datastore_search?resource_id=fbf9a5c6-2e4c-4cb4-a996-7f9859df0a6c](https://data.boston.gov/api/3/action/datastore_search?resource_id=fbf9a5c6-2e4c-4cb4-a996-7f9859df0a6c)

---

### 2. Environnement et dépendances

Création et activation de l’environnement virtuel :

* Commande : `python -m venv env_boston`
* Activation :

  * Windows : `env_boston\Scripts\activate`
  * macOS/Linux : `source env_boston/bin/activate`

Installation des dépendances :

* `pip install pandas numpy pytest`
* `pip freeze > requirements.txt`

Imports utilisés :

* json
* urllib.request
* pandas
* numpy

---

### 3. Étapes du pipeline ETL

Le projet suit le schéma suivant : Extract → Transform → Load → Analyse.

**Étape 1 – Extract**
La fonction `extract_boston_salary(url)` récupère les données JSON depuis l’API de Boston, les convertit en DataFrame et gère les erreurs réseau.

**Étape 2 – Transform**
La fonction `transform(df)` nettoie et prépare les données :

* Conversion des colonnes numériques (regular, overtime, other, total_earnings).
* Création de la colonne total_earnings si elle n’existe pas.
* Nettoyage des noms de colonnes.

**Étape 3 – Load**
La fonction `load(df, filename)` enregistre les données nettoyées dans un fichier CSV local.

**Étape 4 – Analyse**
La fonction `analyse(df)` calcule des statistiques pour chaque département :

* nombre d’employés,
* salaire moyen, médian, minimum et maximum.

---

### 4. Exécution du pipeline

Lancer le pipeline depuis la racine du projet :
`python main.py`

Résultats obtenus :

* Extraction terminée.
* Transformation effectuée.
* Données sauvegardées.
* Statistiques calculées par département.
* Pipeline exécuté avec succès.

Fichiers générés :

* boston_salaries_clean.csv
* department_stats.csv

---

### 5. Organisation selon la méthode AGILE

**Vision produit :**
Créer un pipeline ETL automatisé, testé et réutilisable pour analyser les données publiques de la ville de Boston selon les principes DataOps (qualité, fiabilité, traçabilité).

**Backlog produit :**

1. Extraction des données depuis l’API Boston.
2. Nettoyage et transformation des données.
3. Sauvegarde des données nettoyées (CSV).
4. Analyse statistique.
5. Tests unitaires et CI/CD.
6. Documentation du projet et dépôt sur GitHub.

**Sprints :**

* Sprint 1 : Extraction + Transformation (3 jours)
* Sprint 2 : Load + Analyse (3 jours)
* Sprint 3 : Tests + CI/CD + Documentation (2 jours)

**Rôles et responsabilités :**

* Gloire BOUNGOU : Scrum Master / Développeur principal – coordination, intégration, CI/CD
* Valence OKO : Développeuse – extraction et transformation des données
* Ann-Jireh MVOUTOU : Développeuse – analyse statistique
* Louma LIBIZANGOMO : Développeuse – documentation et relecture
* Arcy MIAMBANZILA : Développeur – support technique et optimisation

**Rituels d’équipe :**

* Daily meeting : 5 minutes pour suivre l’avancement
* Sprint review : présentation des livrables
* Rétrospective : amélioration continue

**Outils utilisés :**
VS Code, Git/GitHub, Python (pandas, numpy), Pytest, GitHub Actions, Microsoft Teams.

---

### 6. Tests unitaires (Pytest)

Les tests unitaires assurent la fiabilité du pipeline ETL.

Tests effectués :

* `test_extract_returns_dataframe()` : vérifie le format DataFrame.
* `test_transform_creates_total_earnings()` : vérifie la création de la colonne total_earnings.
* `test_analyse_returns_stats()` : vérifie la cohérence des statistiques.

Commande d’exécution des tests :
`pytest -v`

Résultat attendu :
3 tests exécutés et validés avec succès.

---

### 7. Automatisation CI/CD – GitHub Actions

Un workflow CI/CD a été créé dans `.github/workflows/ci.yml` pour automatiser les tests à chaque push sur la branche principale.

Contenu du fichier ci.yml :

* Installation des dépendances.
* Lancement automatique de `pytest -v`.
* Validation du pipeline sur GitHub.

Chaque mise à jour du dépôt déclenche un test automatique et confirme que le projet reste fonctionnel.

---

### 8. Cycle de vie des données (DataOps)

Le pipeline respecte le cycle complet de la méthodologie DataOps :

1. Ingestion (Extract) – récupération automatique depuis l’API.
2. Transformation – nettoyage et typage des données.
3. Stockage (Load) – sauvegarde dans un CSV.
4. Analyse – génération de statistiques.
5. Validation – tests unitaires Pytest.
6. Automatisation – intégration continue via GitHub Actions.
7. Documentation – README complet et clair.

Ce processus garantit la traçabilité, la reproductibilité et la qualité continue du projet.

---

### 9. Livraison finale

Éléments livrés :

* Lien GitHub du projet : [[https://github.com/glo007/dataops-boston](https://github.com/glo007/dataops-boston)](https://github.com/glo007/project_data.git)
* Dernier commit : 15/10/2025
* CI/CD GitHub Actions : opérationnelle
* Pipeline ETL : fonctionnel de bout en bout
* Documentation : complète
* Rendu Teams : effectué dans les délais

---


---
