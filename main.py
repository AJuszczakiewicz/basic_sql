from presentation import *
from data_manager import *


while True:
    print_questions(questions)
    print("Or select 'q' to quit")
    option = input("Use number to pick option: ")
    if option == 'q':
        exit()
    elif option == '1':
        print("\n", questions[option])
        print_table(mentors_first_last_name())
    elif option == '2':
        print("\n", questions[option])
        print_table(mentors_who_work_at_miskolc_nicks())
    elif option == '3':
        print("\n", questions[option])
        print_table(carol_full_name_phone())
    elif option == '4':
        print("\n", questions[option])
        print_table(girl_with_adipiscingenimmi_email())
    elif option == '5':
        print("\n", questions[option])
        insert_markus_schaffarzyk()
        print_table(view_markus_schaffarzyk())
    elif option == '6':
        print("\n", questions[option])
        update_jemima_foreman_phone()
        print_table(view_jemina_foreman())
    elif option == '7':
        print("\n", questions[option])
        delete_mauriseu_applicants(find_mauriseu_applicants())
        print_table(show_all_applicants())
