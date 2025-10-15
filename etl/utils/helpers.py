import json
import urllib.request
import pandas as pd
import numpy as np

def extract_boston_salary(url: str) -> pd.DataFrame:
    """Extrait les données brutes depuis l’API publique de Boston."""
    with urllib.request.urlopen(url) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    records = data["result"]["records"]
    df = pd.DataFrame(records)
    return df

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoie et prépare les données de salaires."""
    numeric_cols = ["regular", "overtime", "other", "total_earnings"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # Création du salaire total si manquant
    if "total_earnings" not in df.columns and all(c in df.columns for c in ["regular", "overtime", "other"]):
        df["total_earnings"] = df["regular"] + df["overtime"] + df["other"]

    # Nettoyage des noms de colonnes
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df

def load(df: pd.DataFrame, filename: str):
    """Enregistre les données transformées dans un fichier CSV."""
    df.to_csv(filename, index=False)


def analyse(df: pd.DataFrame) -> pd.DataFrame:
    """Réalise des statistiques par département."""
    if "department_name" not in df.columns:
        dept_col = [c for c in df.columns if "dept" in c.lower()]
        if not dept_col:
            raise ValueError("Aucune colonne de département trouvée.")
        dept_col = dept_col[0]
    else:
        dept_col = "department_name"

    stats = (
        df.groupby(dept_col)["total_earnings"]
        .agg(["count", "mean", "min", "max", "median"])
        .sort_values("mean", ascending=False)
    )
    return stats
