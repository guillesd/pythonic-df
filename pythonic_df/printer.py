from tabulate import tabulate
from pythonic_df.data_structures import DataFrame

def pretty_print(df: DataFrame) -> None:
    """Pretty prints a DataFrame structure using tabulate"""
    input = {"index": df.index}
    for col in df.columns:
        input[col.name] = col.values

    print(tabulate(input, headers="keys"))
