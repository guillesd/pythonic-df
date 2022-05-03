from dataclasses import dataclass, field
from typing import Dict, List, Union

@dataclass
class Column:
    """
    Dataclass that represents a column
    """
    name: str
    data_type: Union[str, int, float, bool]
    values: List
    length: int = field(init=False)
    
    def __post_init__(self):
        self.length = self._add_length()
        self._check_typing()

    def _add_length(self):
        return len(self.values)

    def _check_typing(self):
        if all(isinstance(val, self.data_type) for val in self.values):
            pass
        else:
            raise AttributeError(
                f"Expected values to be of type {self.data_type} but found {type(self.values[0])}"
            )


@dataclass
class DataFrame:
    """
    Dataclass that represents a dataframe
    """
    columns: List[Column]
    index: List[int] = field(init=False)

    def __post_init__(self):
        self._same_size_columns()
        self.index = self._set_index()

    def _same_size_columns(self):
        lengths = [col.length for col in self.columns]
        if max(lengths) != min(lengths):
            raise ValueError("Column sizes are not the same.")

    def _set_index(self):
        return list(range(self.columns[0].length))

    def get_row(self, index_value: int) -> Dict:
        return {col.name:col.values[index_value] for col in self.columns}

    def get_column(self, column_name: str) -> Column:
        for col in self.columns:
            if col.name == column_name:
                return col 
        raise ValueError(f"There are no columns named {column_name}")
    