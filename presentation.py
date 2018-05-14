from data_manager import *
from terminaltables import AsciiTable


def get_headers(list_of_dictionaries):
    return [key for key in list_of_dictionaries[0]]


def print_table(headers, data):
    table_data = [headers]
    for item in data:
        table_data.append(item.values())
    table = AsciiTable(table_data)
    print(table.table)


