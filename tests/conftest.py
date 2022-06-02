import pytest

from pythonic_df.data_structures import DataFrame, Column

@pytest.fixture
def dataframe():
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
    return DataFrame([col_a, col_b, col_c])