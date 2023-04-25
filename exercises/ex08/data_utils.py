__author__ = "730485079"

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close
    return result

def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    #step through table
    for row in table:
        #save every value under key "header"
        result.append(row[header])
    return result

def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers."""
    result: dict[str, list[str]] = {}
    #loop through keys of one row of table
    first_row: dict[str, str] = table[0]
    for key in first_row:
        #for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result

def head(inputhead: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Makes crazy large table with all the data."""
    result: dict[str, list[str]] = {}
    for item in inputhead:
        darows: list[str] = []
        for i in range(min(rows, len(inputhead[item]))):
            darows.append(inputhead[item][i])
        result[item] = darows
    return result

def select(table: dict[str, list[str]], thelist: list[str]) -> dict[str, list[str]]:
    """Will only show you the specific values of a particular table."""
    result: dict[str, list[str]] = {}
    for item in thelist:
        result[item] = table[item]
    return result

def concat(input1: dict[str, list[str]], input2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Takes two tables and smashes them into one."""
    result: dict[str, list[str]] = {}
    for item in input1:
        result[item] = input1[item]
    for item in input2:
        if item in result:
            result[item].extend(input2[item])
        else:
            result[item] = input2[item]
    return result

def count(nmberoftimes: list[str]) -> dict[str, int]:
    """Counts number of times certain values appear."""
    result: dict[str, int] = {}
    for item in nmberoftimes:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result