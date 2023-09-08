from src.etl.Transform import Transfrom
import pandas as pd

def test_string_columns_in_pandas_dataframe_are_converted_to_lowercase():
    test_df = pd.DataFrame({"test_string_data": ["Testing", "one", "TWO", "ThreE", None], "test_numbers": [1,2,3,4,5]})
    expected_df = pd.DataFrame({"test_string_data": ["testing", "one", "two", "three", None], "test_numbers": [1,2,3,4,5]})

    df_result = Transfrom.lowercase_strings(test_df)

    assert expected_df.equals(df_result)

def test_string_columns_in_pandas_dataframe_are_stripped_of_whitespace():
    test_df = pd.DataFrame({"test_string_data": [" Testing", " on e", " TWO ", " ThreE", None], "test_numbers": [1,2,3,4,5]})
    expected_df = pd.DataFrame({"test_string_data": ["Testing", "on e", "TWO", "ThreE", None], "test_numbers": [1,2,3,4,5]})

    df_result = Transfrom.strip_strings(test_df)
    print(df_result["test_string_data"].to_list())

    assert expected_df.equals(df_result)

def test_column_data_is_masked():
    test_df = pd.DataFrame({"test_string_data": [" Testing", "one", "one", " ThreE", None], "test_numbers": [1,2,3,4,5]})
    expected_df = pd.DataFrame({"test_string_data": [0, 2, 2, 1, -1], "test_numbers": [1,2,3,4,5]})

    df_result = Transfrom.mask_category(test_df, "test_string_data")
    print(df_result)
    print(expected_df)

    assert expected_df.equals(df_result)
