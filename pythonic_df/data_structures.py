from dataclasses import dataclass, field
from multiprocessing.sharedctypes import Value
from ntpath import join
from typing import Dict, List, Tuple, Union
from collections import defaultdict

@dataclass
class Column:
    """
    Dataclass that represents a column
    """
    name: str
    values: List
    data_type: Union[str, int, float, bool, None] = None
    length: int = field(init=False)
    
    def __post_init__(self):
        self.length = self._add_length()
        self._add_typing()
        self._check_typing()

    def _add_length(self):
        return len(self.values)

    def _add_typing(self):
        if self.data_type == None:
            self.data_type = type(self.values[0])
        else:
            pass

    def _check_typing(self):
        if all(isinstance(val, self.data_type) for val in self.values):
            pass
        else:
            types_found = set([type(v) for v in self.values])
            raise AttributeError(
                f"Expected values of column {self.name} to be of type {self.data_type} but found {*types_found,}"
            )


@dataclass
class DataFrame:
    """
    Dataclass that represents a dataframe
    """
    columns: List[Column]
    index: List[int] = field(init=False)
    column_names: List[str] = field(init=False)

    def __post_init__(self):
        self._same_size_columns()
        self.index = self._set_index()
        self.column_names = self._set_column_names()
        self._check_column_name_collision()

    def __dict__(self):
        return {col.name:col.values for col in self.columns}

    def _set_column_names(self) -> List[str]:
        return [col.name for col in self.columns]

    def _same_size_columns(self):
        lengths = [col.length for col in self.columns]
        if max(lengths) != min(lengths):
            raise ValueError("Column sizes are not the same.")

    def _set_index(self):
        return list(range(self.columns[0].length))

    def _check_column_name_collision(self):
        col_names = [col.name for col in self.columns]
        if len(set(col_names)) != len(col_names):
            raise ValueError(f"You cannot have repeated column names, this will create collisions")

    def get_row(self, index_value: int) -> Dict:
        return {col.name:col.values[index_value] for col in self.columns}

    def get_column(self, column_name: str) -> Column:
        for col in self.columns:
            if col.name == column_name:
                return col 
        raise ValueError(f"There are no columns named {column_name}")

    def get_rows_as_tuples(self) -> List[Tuple]:
        """
        Returns a DataFrame as a list of rows. Each tuple is a row, e.g.:
        [(1, 'a', 2.3), (2, 'b', 3.1)]
        """
        l = list()
        for col in self.columns:
            l.append(col.values)
        return list(zip(*l))

    def get_hash_table(self, key: str) -> Dict[str, List[Tuple]]:
        """
        Returns the hash table of the DataFrame based on the provided key, e.g.:
            df1 = dataframe_from_dict({'col_a': [1, 2, 1], 'col_b': [2, 4, 3]})
            print(df1.get_hash_table("col_a"))
        which prints:
            {1: [(1, 2), (1, 3)], 2: [(2, 4)]}
        """
        h = defaultdict(list)
        rows = self.get_rows_as_tuples()
        key_column = self.get_column(key).values
        for k,r in zip(key_column, rows):
            h[k].append(r)
        return h

    