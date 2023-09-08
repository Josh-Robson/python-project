import pandas as pd

def save_datafame_to_jsonl_file(df: pd.DataFrame, file_path: str):
    with open(file_path, "w") as file:
        file.write(df.to_json(orient="records", lines=True))