# 🏙️ Projet TP – ETL : Analyse des écarts de salaires à Boston

**Auteurs :**  
- 🧑‍💻 Valence OKO  
- 🧑‍💻 Gloire BOUNGOU *(Responsable du repo GitHub)*  
- 🧑‍💻 Ann-Jireh MVOUTOU  
- 🧑‍💻 Louma LIBIZANGOMO  

**Date :** 15 octobre 2025  
**Encadrant :** Antoine Lucsko  
**Cours :** DataOps – BTS SIO / Parcours Data & App Design  

---

## 🎯 1. Contexte

L’objectif de ce projet est de **mettre en œuvre un pipeline ETL complet** (Extract, Transform, Load) pour analyser les **écarts de salaires** des employés municipaux de la ville de **Boston (2018)**.  

Le but est de :
- Extraire les données depuis une **API publique**  
- Les transformer pour les rendre exploitables  
- Les charger dans un **fichier CSV propre**  
- Calculer des **statistiques par département** (min, max, moyenne, médiane, etc.)

**Source des données :**  
[City of Boston Payroll Data (API)](https://data.boston.gov/api/3/action/datastore_search?resource_id=fbf9a5c6-2e4c-4cb4-a996-7f9859df0a6c)

---

## ⚙️ 2. Environnement et dépendances

Créer et activer l’environnement virtuel :

```bash
python -m venv env_boston
env_boston\Scripts\activate        # Windows
# ou
source env_boston/bin/activate     # macOS / Linux
