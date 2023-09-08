import pandas as pd
import os
from src.etl.load_file import save_datafame_to_jsonl_file

def test_save_data_converts_pandas_df_to_jsonl_and_saves_file():
    test_file_path = "./test_save.jsonl"
    test_df = pd.DataFrame({"test":[1,2,3], "data": ["one", "two", "three"]})

    save_datafame_to_jsonl_file(test_df, test_file_path)

    assert os.path.isfile(test_file_path)
    with open(test_file_path, "r") as file:
        lines = [line for line in file]
        assert '{"test":1,"data":"one"}\n' == lines[0]
        assert '{"test":2,"data":"two"}\n' == lines[1]
        assert '{"test":3,"data":"three"}\n' == lines[2]
    os.remove(test_file_path)