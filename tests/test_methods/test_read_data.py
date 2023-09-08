from src.etl.read_data import read_data_from_csv
import os
import pandas as pd
import pytest

@pytest.fixture
def csv_file_path():
    return "C:/Users/Josh/Documents/Python/Interview/tests/test_data/test_csv.csv"

def test_read_data_returns_pandas_dataframe_when_provided_csv(csv_file_path):
    expected_headers = ["PassengerId", "Survived", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin Embarked"]
    expected_name = "Braund, Mr. Owen Harris"
    result = read_data_from_csv(csv_file_path)
    print(f"names: {result['Name']}")

    assert len(result.columns) == 12
    assert expected_name in result["Name"].to_list()
    assert result.columns.to_list().sort() == expected_headers.sort()
