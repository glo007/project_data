from etl.utils.helpers import extract_boston_salary, transform, load, analyse

URL = (
  "https://data.boston.gov/api/3/action/datastore_search?resource_id=31358fd1-849a-48e0-8285-e813f6efbdf1"

)

def main():
    print("=== PIPELINE ETL : SALAIRES BOSTON ===")

    df_raw = extract_boston_salary(URL)
    print(f"✅ Extraction terminée ({len(df_raw)} lignes)")

    df_clean = transform(df_raw)
    print("✅ Transformation effectuée")

    load(df_clean, "boston_salaries_clean.csv")
    print("✅ Données sauvegardées")

    stats = analyse(df_clean)
    print("\n=== STATISTIQUES PAR DÉPARTEMENT ===")
    print(stats.head())

    print("\nPipeline exécuté avec succès 🎯")

if __name__ == "__main__":
    main()
