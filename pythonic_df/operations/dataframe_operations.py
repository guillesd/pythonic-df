from audioop import reverse
from pythonic_df.data_structures import DataFrame, Column
from pythonic_df.utils import dataframe_from_dict, rows_to_dataframe, patch_name_collisions

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

def join(df1: DataFrame, df2: DataFrame, key1: str, key2: str, type: str) -> DataFrame:
    """
    Joins two DataFrames. Accepts left, inner and outer join.
    """
    accepted_types = ['left', 'inner', "outer"]
    if type not in accepted_types:
        raise AttributeError(f"Type {type} is not in the list of supported joins: {*accepted_types,}")

    elif type == 'inner':
        return _inner_join(df1, df2, key1, key2)

    else:
        pass

def _inner_join(df1: DataFrame, df2: DataFrame, key1: str, key2: str) -> DataFrame:
    """
    Inner joins two DataFrames using the hash join algorithm
    """
    tb1_hash = df1.get_hash_table(key1)
    tb2_hash = df2.get_hash_table(key2)
    inner = list()

    for key in tb1_hash.keys():
        inner.extend([row_tb1 + row_tb2 for row_tb1 in tb1_hash[key] for row_tb2 in tb2_hash[key]])
    
    column_names = patch_name_collisions(df1.column_names + df2.column_names)

    return rows_to_dataframe(rows=inner, column_names=column_names)