from pythonic_df.data_structures import Column, DataFrame
from pythonic_df.utils import dataframe_from_dict, enforce_typing
from typing import Union, List, Dict
import csv

def read_csv(file_path: str, delimiter: str, has_headers: bool = False, column_names: Union[List, None] = None, data_types: Union[Dict[str, type], None] = None) -> DataFrame:
    """Method that reads a csv file and formats the data into a pythonic_df DataFrame object"""
    with open(file_path, "r") as file:
        contents = csv.reader(file, delimiter=delimiter)

        # assign headers
        headers = list()
        if column_names != None:
            headers = column_names            
        elif has_headers:
            headers = next(contents)  
        content_list = [row for row in contents]
        if not headers:
            headers = [str(i) for i in range(content_list[0])]


        # get list of Columns and return DataFrame    
        df = _format_into_dataframe(data=content_list, headers=headers)

        # enforce data types
        if data_types:
            df = enforce_typing(df=df, types=data_types)

        return df
        

def _format_into_dataframe(data: List[List], headers: List) -> DataFrame:
    """
    Method that takes the data in the form of a List of rows and a separate list of headers
    and transforms it into a list of pythonic_df columns.
    """
    output_dict = {h:[] for h in headers}
    for row in data:
        for i in range(len(headers)):
            output_dict[headers[i]].append(row[i])
    return dataframe_from_dict(output_dict)
    
            

