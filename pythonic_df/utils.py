from pythonic_df.data_structures import Column, DataFrame
from typing import Dict, List, Tuple

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

def rows_to_dataframe(rows: List[Tuple], column_names: List[str]) -> DataFrame:
    """
    Takes in a list of rows like: [('a', 1, 3.4), ('b', 2, 3.1)]
    and transforms it into a pythonic DataFrame
    """
    transposed = list(map(list, zip(*rows)))
    column_list = list()
    for i, col in enumerate(transposed):
        column_list.append(
            Column(
                name=column_names[i],
                data_type=type(col[0]),
                values=col
            )
        )
    return DataFrame(column_list)

def patch_name_collisions(names: List[str]):
    """
    Simple algorithm to remove duplicated names in columns.
    """
    seen = list()
    output = list()
    for name in names:
        if name not in seen:
            seen.append(name)
            output.append(name)
        else:
            seen.append(name)
            output.append(f"{name}_{seen.count(name)}")
    
    return output


def dataframe_from_dict(input: Dict[str, List]) -> DataFrame:
    """Wraps _dict_to_columns into a DataFrame"""
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
