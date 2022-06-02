from pythonic_df.data_structures import DataFrame
from pythonic_df.utils import dataframe_from_dict

def append(base_df: DataFrame, another_df: DataFrame) -> DataFrame:
    """
    Appends one dataframe to another
    """
    base_dict = base_df.__dict__()
    for name, values in another_df.__dict__().items():
        base_dict[name].extend(values)

    return dataframe_from_dict(base_dict)