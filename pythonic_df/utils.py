from pythonic_df.data_structures import Column, DataFrame
from typing import Dict, List

def _dict_to_columns(input: Dict[str, List]) -> List[Column]:
    """
    Gets a Dictionary with format like:
    {'col_a': [1, 2], 'col_b': [2, 4]}
    And converts it into a List[Column]
    *Note: This method infers data types, don't use it if that is not intended
    """
    output = list()
    for key, values in input.items():
        output.append(
            Column(
                name=key,
                data_type=type(values[0]),
                values=values
            )
        )
    return output

def dataframe_from_dict(input: Dict[str, List]) -> DataFrame:
    return DataFrame(_dict_to_columns(input=input))

def enforce_typing(df: DataFrame, types: Dict[str, type]) -> DataFrame:
    """
    Takes a DataFrame and a dictionary containing {column_name: python_type} 
    and enforces this typing into the DataFrame columns. 
    This operation is in place.
    """
    for i in range(len(df.columns)):
        df.columns[i].data_type = types[df.columns[i].name]
    
    return df
