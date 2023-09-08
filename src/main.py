from etl.Transform import Transfrom
from etl.load_file import save_datafame_to_jsonl_file
from etl.read_data import read_data_from_csv

def main():
    raw_data = read_data_from_csv("./titanic.csv")
    try:
        data_stripped = Transfrom.strip_strings(raw_data)
        data_lowered = Transfrom.lowercase_strings(data_stripped)
    except:
        Exception("unable to tranform, data error with the dataset provided")
    save_datafame_to_jsonl_file(data_lowered, "./prepped_titanic_data.jsonl")

if __name__ == "__main__":
    main()