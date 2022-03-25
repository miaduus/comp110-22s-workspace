"""Dictionary related utility functions."""

__author__ = "730464966"

from csv import DictReader

# read_cvs_rows, column_values, columnar  from lessons about CVS file reading


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
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
    # Loop through each of columns in first row
    for key in column_table:
        result_list: list[str] = []
        # Access value from column table that is a list of strings
        a_list: list[str] = []
        a_list = column_table[key]
        i: int = 0
        # If N is larger than the actual number of rows, returns all rows
        if len(column_table[key]) < N:
            N = len(column_table[key])
        # Use while loop to append only the N amount of rows
        while i < N:
            result_list.append(a_list[i])
            i += 1
        result[key] = result_list
    return result


def select(column_table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce new column based table with only specific subsets of original columns."""
    result: dict[str, list[str]] = {}
    # Loop through the different names/items in the list of column names
    for item in names:
        # Access list that are the value from the key-value pair in the column table
        a_list: list[str] = []
        a_list = column_table[item]
        # Add the key-value pair to the result dictionary
        result[item] = a_list
    return result


def concat(a_table: dict[str, list[str]], b_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce new column table that are the combination of table a and b."""
    result: dict[str, list[str]] = {}
    # Loop through first table parameter
    for a_key in a_table:
        a_list: list[str] = []
        # Access value that are a list for the given key and add this key-value pair to the dict
        a_list = a_table[a_key]
        result[a_key] = a_list
    # Loop through secon table parameter
    for b_key in b_table:
        # If key is already in result, the list for the key in the second dict is added to the list of strings in result dict
        if b_key in result:
            b_list: list[str] = []
            b_list = b_table[b_key]
            result[b_key] += b_list
        # Else the key and it's value in form of a list of strings is added to the result dict
        else:
            c_list: list[str] = []
            c_list = b_table[b_key]
            result[b_key] = c_list
    return result


def count(values: list[str]) -> dict[str, int]:
    """Function that creates list of values and the number of times the value appear in list."""
    result: dict[str, int] = {}
    # Loop through the items in the list of strings
    for items in values:
        # If the item already exist as a key in result dictionary, the value is increased by 1
        if items in result:
            result[items] += 1
        # Else the item is set as a key and value set as 1
        else:
            result[items] = 1
    return result