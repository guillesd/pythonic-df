import pytest

from pythonic_df.data_structures import Column, DataFrame

def test_dataframe_constructor():
    col_a = Column(
    name = "Numbers",
    data_type = int,
    values = [1, 2, 4]
    )

    col_b = Column(
        name = "Letters",
        data_type = str,
        values = ["a", "b", "d"]
    )

    col_c = Column(
        name = "Booleans",
        data_type = bool,
        values = [True, False, True]
    )
    DataFrame([col_a, col_b, col_c])

#column stuff
def test_column_check_typing():
    with pytest.raises(AttributeError):
        col_b = Column(
        name = "Letters",
        data_type = str,
        values = ["a", "b", 1]
        )

def test_column_add_typing():
    col_b = Column(
        name = "Letters",
        values = ["a", "b", "c"]
    )
    assert col_b.data_type == str

def test_column_lenght():
    col_b = Column(
        name = "Letters",
        values = ["a", "b", "c"]
    )
    assert col_b.length == 3

#dataframe stuff, using fixtures in conftest when possible
def test_dunder_dict(dataframe):
    dict_df = {'Numbers': [1, 2, 4], 'Letters': ['a', 'b', 'd'], 'Booleans': [True, False, True]}
    assert dataframe.__dict__() == dict_df

def test_same_size_columns():
    col_a = Column(
    name = "Numbers",
    data_type = int,
    values = [1, 2, 4]
    )

    col_b = Column(
        name = "Letters",
        data_type = str,
        values = ["a", "b"]
    )
    with pytest.raises(ValueError):
        DataFrame([col_a, col_b])

def test_get_row_from_dataframe(dataframe):
    expected = {'Numbers': 1, 'Letters': 'a', 'Booleans': True}
    row = dataframe.get_row(0)

    assert row == expected

def test_get_column_from_dataframe(dataframe):
    expected = Column(
        name = "Numbers",
        data_type = int,
        values = [1, 2, 4]
    )
    col = dataframe.get_column('Numbers')

    assert expected == col

def test_dataframe_column_collision(dataframe):
    col_1 = Column(
        name = "Numbers",
        data_type = int,
        values = [1, 2, 4]
    )
    col_2 = Column(
        name = "Numbers",
        data_type = int,
        values = [1, 2, 4]
    )
    with pytest.raises(Exception):
        DataFrame([col_1, col_2])
