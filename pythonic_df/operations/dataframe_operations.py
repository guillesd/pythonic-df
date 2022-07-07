from pythonic_df.data_structures import DataFrame, Column
from pythonic_df.utils import dataframe_from_dict

from typing import List

def append(base_df: DataFrame, another_df: DataFrame) -> DataFrame:
    """
    Appends one dataframe to another
    """
    base_dict = base_df.__dict__()
    for name, values in another_df.__dict__().items():
        base_dict[name].extend(values)

    return dataframe_from_dict(base_dict)

def add_columns(df: DataFrame, columns: List[Column]):
    """
    Creates a new DataFrame with the columns from the original DataFrame 
    plus the List of additional columns
    """
    for col in columns:
        if not isinstance(col, Column):
            raise ValueError(f"Column {col} is not of Column type")
    return DataFrame(df.columns.extend(columns))

def concat(dataframes: List[DataFrame]) -> DataFrame:
    """
    Receives a list of DataFrame and concatenates them into one DataFrame object
    """
    output_df = None
    for df in dataframes:
        if isinstance(df, DataFrame):
            if output_df == None:
                output_df = df
            else:
                output_df = append(output_df, df) 

    return output_df
