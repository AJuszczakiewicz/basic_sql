from terminaltables import AsciiTable


def get_headers(list_of_dictionaries):
    return [key for key in list_of_dictionaries[0]]


def print_table(data):
    table_data = [get_headers(data)]
    for item in data:
        table_data.append(item.values())
    table = AsciiTable(table_data)
    print(table.table)


questions = {
    '1': 'Show list of mentors',
    '2': 'Show nick_name-s of all mentors working at Miskolc.',
    '3': 'Show Carol full name and phone number info',
    '4': 'Show hat girl info from Adipiscingenimmi University',
    '5': 'Add Markus Schaffarzyk applicant',
    '6': 'Update Jemima Foreman phone number to: 003670/223-7459',
    '7': 'Delate all mauriseu\'s applicants'
}


def print_questions(dictionary_questions):
    for key, value in dictionary_questions.items():
        print("{}: {}".format(key, value))

