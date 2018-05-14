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


@connection_handler
def mentors_who_work_at_miskolc_nicks(cursor):
    cursor.execute("""
                    SELECT nick_name FROM mentors
                    WHERE city = 'Miskolc';
                  """)
    mentors = cursor.fetchall()
    return mentors


@connection_handler
def carol_full_name_phone(cursor):
    cursor.execute("""
                    SELECT first_name||' '||last_name AS full_name, phone_number
                    FROM applicants
                    WHERE first_name = 'Carol';
                  """)
    carol = [cursor.fetchone()]
    return carol


@connection_handler
def girl_with_adipiscingenimmi_email(cursor):
    cursor.execute("""
                    SELECT first_name||' '||last_name AS full_name, phone_number
                    FROM applicants
                    WHERE email LIKE '%@adipiscingenimmi.edu'
                  """)
    hat_girl = [cursor.fetchone()]
    return hat_girl


@connection_handler
def insert_markus_schaffarzyk(cursor):
    cursor.execute("""
                    INSERT INTO applicants(first_name, last_name, phone_number, email, application_code)
                    VALUES('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823)
                  """)


@connection_handler
def view_markus_schaffarzyk(cursor):
    cursor.execute("""
                      SELECT * FROM applicants 
                      WHERE application_code = 54823
                  """)
    markus = [cursor.fetchone()]
    return markus


@connection_handler
def update_jemima_foreman_phone(cursor):
    cursor.execute("""
                    UPDATE applicants
                    SET phone_number = '003670/223-7459'
                    WHERE first_name = 'Jemima' and last_name = 'Foreman'
                  """)


@connection_handler
def view_jemina_foreman(cursor):
    cursor.execute("""
                    SELECT first_name||' '||last_name AS full_name, phone_number
                    FROM applicants
                    WHERE first_name = "Jemima" and last_name = "Foreman"
                  """)
    jemima = [cursor.fetchone()]
    return jemima


@connection_handler
def find_mauriseu_applicants(cursor):
    cursor.execute("""
                    SELECT id FROM applicants
                    WHERE email LIKE '%@mauriseu.net' 
                  """)
    applicants = cursor.fetchall()
    applicants_id = []
    for item in applicants:
        applicants_id.append(item['id'])
    return applicants_id


@connection_handler
def delete_mauriseu_applicants(cursor, applicants_id):
    for id in applicants_id:
        cursor.execute("""
                        DELETE FROM applicants
                        WHERE id=%s
                      """, (id,))


@connection_handler
def show_all_applicants(cursor):
    cursor.execute("""SELECT * FROM applicants""")
    all_applicants = cursor.fetchall()
    return all_applicants
