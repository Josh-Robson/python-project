import pandas as pd

def read_data_from_csv(path: str) -> pd.DataFrame:
    """
    This function is used to read raw csv data provided to the application into a pandas DataFrame.

    args:
        path (str): A path to the raw csv file.
    
    returns:
        pd.DataFrame: a pandas dataframe containing the csv data.
    
    raises:
        Exception: raises exception when unable to read the file.

    """
    try:
        raw_data = pd.read_csv(path)
        return raw_data
    except:
        Exception(message=f"Could not read file, path provided: {path}")