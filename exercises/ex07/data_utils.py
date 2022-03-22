"""Dictionary related utility functions."""

__author__ = "730464966"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rowws of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    # We assume there is at least one row
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(column_table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first N rows of data from each column."""
    result: dict[str, list[str]] = {}
    for column in column_table:
        result_list: list[str] = []
        for items in column:
            # problem that the column names are being put in as column data
            result_list.append(items)
            result[column] = result_list
    return result


def select_function(column_table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce new column based table with only specific subsets of original columns."""
    result: dict[str, list[str]] = {}
    # write code
    return result


def concat(a_table: dict[str, list[str]], b_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce new column table that are the combination of table a and b."""
    result: dict[str, list[str]] = {}
    # write code
    return result


def count(values: list[str]) -> dict[str, int]:
    """Function that creates list of values and the number of times the value appear in list."""
    result: dict[str, int] = {}
    return result