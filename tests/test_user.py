import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from etl.utils.helpers import extract_boston_salary, transform, analyse

URL = (
   "https://data.boston.gov/api/3/action/datastore_search?resource_id=31358fd1-849a-48e0-8285-e813f6efbdf1"

)

def test_extract_returns_dataframe():
    df = extract_boston_salary(URL)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_transform_creates_total_earnings():
    df = pd.DataFrame({
        "regular": [100, 200],
        "overtime": [10, 20],
        "other": [5, 10]
    })
    df_clean = transform(df)
    assert "total_earnings" in df_clean.columns

def test_analyse_returns_stats():
    df = pd.DataFrame({
        "department_name": ["Police", "Police", "Fire"],
        "total_earnings": [100, 200, 300]
    })
    result = analyse(df)
    assert "mean" in result.columns
    assert "Police" in result.index
