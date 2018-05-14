from config import config
import psycopg2
import psycopg2.extras


def open_database():
    connection = None
    try:
        params = config()
        connection = psycopg2.connect(**params)
        connection.autocommit = True

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return connection


def connection_handler(funct):
    def wrapper(*args, **kwargs):
        connection = open_database()
        # we set the cursor_factory parameter to return with a RealDictCursor cursor (cursor which provide dictionaries)
        dict_cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        ret_value = funct(dict_cursor, *args, **kwargs)
        dict_cursor.close()
        connection.close()
        return ret_value

    return wrapper



@connection_handler
def mentors_first_last_name(cursor):
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors;
                   """)
    mentors = cursor.fetchall()
    return mentors

