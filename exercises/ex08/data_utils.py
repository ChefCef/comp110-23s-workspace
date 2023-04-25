from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys"""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close
    return result

def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header"""
    result: list[str] = []
    #step through table
    for row in table:
        #save every value under key "header"
        result.append(row[header])
    return result

def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers"""
    result: dict[str, list[str]] = {}
    #loop through keys of one row of table
    first_row: dict[str, str] = table[0]
    for key in first_row:
        #for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result

def head(inputhead: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for row in inputhead:
        darow: list[str] = []
        for i in range(min(rows, len(inputhead[row]))):
            darow.append(inputhead[row][i])
        result[row] = darow
    return result

def select(table: dict[str, list[str]], thelist: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for row in thelist:
        result[row] = table[row]
    return result

def concat(input1: dict[str, list[str]], input2: dict[str, list[str]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for column in input1:
        result[column] = input1[column]
    for column in input2:
        if column in result:
            result[column].extend(input2[column])
        else:
            result[column] = input2[column]
    return result