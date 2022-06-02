## pythonic-df

Making a native python DataFrame library from scratch, just for fun!

## Usage

### Installation
You can install this package via pip:
```bash
pip install https://github.com/guillesd/pythonic-df.git
```

### Creating a DataFrame

The most basic way of doing this is by defining Columns and passing on a List of this to the DataFrame constructor, i.e.:

```python
from pythonic_df.data_structures import Column, DataFrame

col_a = Column(
    name = "Numeros",
    data_type = int,
    values = [1, 2, 4]
)

col_b = Column(
    name = "Letras",
    data_type = str,
    values = ["a", "b", "d"]
)

col_c = Column(
    name = "Boleano",
    data_type = bool,
    values = [True, False, True]
)

df = DataFrame([col_a, col_b, col_c])
```

Of course, this is not something that you usually would do. The most convenient way of creating a DataFrame would be from a dictionary...

```python
from pythonic_df.utils import dataframe_from_dict
pretty_print(dataframe_from_dict({'col_a': [1, 2], 'col_b': [2, 4]}))
```

... or by reading a file in, let's say, .csv format:

```python
from pythonic_df.io.csv import read_csv

df = read_csv(
    file_path="./data/example.csv",
    delimiter=",",
    has_headers=True,
    data_types={"col_a": int, "col_b": str}
)
```

### Displaying your DataFrame

By default, the DataFrame will display as an instance of a python dataclass. Meaning if you just type `print(df)` the output would be something like:

```
[out]: DataFrame(columns=[Column(name='col_a', data_type=<class 'int'>, values=['1', '2', '3'], length=3), Column(name='col_b', data_type=<class 'str'>, values=['a', 'b', 'c'], length=3)], index=[0, 1, 2])
```

This is obviously not a nice way of visualizing your structured data. The better approach would be to use a special printer provided by pythonic-df, like so...

```python
from pythonic_df.printer import pretty_print
pretty_print(df)
```

...which will print out the following:

```
[out]:
      index    col_a  col_b
    -------  -------  -------
          0        1  a
          1        2  b
          2        3  c
```

### DataFrame operations

This module intends to provide an interface to operate with DataFrame structures. Examples of this operations would be:
- Append
- Join
- Group by
- Windowing
- User defined functions
- etc.

An example of how to interact with this module would be:
```python
%autoreload 2
from pythonic_df.operations.dataframe_operations import append

df1 = dataframe_from_dict({'col_a': [1, 2], 'col_b': [2, 4]})
df2 = dataframe_from_dict({'col_a': [7, 8], 'col_b': [9, 11]})
appended_df = append(df1, df2)
pretty_print(appended_df)
```

```
[out]:
      index    col_a    col_b
    -------  -------  -------
          0        1        2
          1        2        4
          2        7        9
          3        8       11
```