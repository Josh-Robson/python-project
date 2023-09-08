import pandas as pd
import numpy as np

class Transfrom():
    def __init__():
        return
    
    def lowercase_strings(df: pd.DataFrame) -> pd.DataFrame:
        """
        Converts string columns in pandas dataframe to lowercase
        """
        df_obj = df.select_dtypes(["object"])
        df[df_obj.columns] = df_obj.apply(lambda x: x.str.lower())
        return df
    
    def strip_strings(df: pd.DataFrame) -> pd.DataFrame:
        """
        Strips the whitespace from both ends of strings in string columns in pandas DataFrame
        """
        df_obj = df.select_dtypes(["object"])
        df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
        return df
    
    def mask_category(df: pd.DataFrame, column: str) -> pd.DataFrame:
        """
        Masks the Dataset category with known values
        """
        masked_df = df.copy()
        unmasked_column = masked_df[column]
        masked_column = unmasked_column.astype('category').cat.codes
        print(masked_column)
        masked_df[column] = masked_column

        return masked_df