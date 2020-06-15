import cx_Oracle as cxo
from model import Model_Class
from view import View_Class
from dto import Dto_Class
import error
M = Model_Class()
V = View_Class()
D = Dto_Class

class Controller_Class:

    def input_data(self):
        D = Dto_Class()
        name = V.input_name()
        phone = Controller_Class.number_except(self)
        email = Controller_Class.email_except(self)
        division = V.input_divison()

        D.set_name(name)
        D.set_phone(phone)
        D.set_email(email)
        D.set_division(division)

        D.get_name()
        D.get_phone()
        D.get_email()
        M.add_contact(D)

    def print_data(self):
        list = M.contact_print()
        V.contact_print(list)

    def delete_data(self):
        name = V.input_name()
        D = Dto_Class()
        D.set_name(name)
        D.get_name()
        del_list = M.delete_contact(D)
        V.contact_delete(del_list)
        delete_name = V.find_index()
        M.delete_model(del_list[delete_name - 1])

    def modify_data(self):
        name = V.input_name()
        D = Dto_Class()
        D.set_name(name)
        D.get_name()
        del_list = M.delete_contact(D)
        V.contact_delete(del_list)
        delete_name = V.find_index()
        M.delete_model(del_list[delete_name - 1])
        name = V.input_name()
        phone = V.input_phone()
        email = V.input_email()
        division = V.input_divison()

        D.set_name(name)
        D.set_phone(phone)
        D.set_email(email)
        D.set_division(division)

        D.get_name()
        D.get_phone()
        D.get_email()
        M.add_contact(D)

    def number_except(self):
        while True:
            num = V.input_phone()
            try:
                num = error.number_error(num)
                return num
            except error.regex_exception as error_n:
                print(error_n)

    def email_except(self):
        while 1:
            email = V.input_email()
            try:
                email = error.email_error(email)
                return email
            except error.regex_exception as error_e:
                print(error_e)


    def run(self):
        while 1:
            try:
                menu = V.mainmenu()
                if menu == 0:
                    V.wrong_input_number()
                elif menu == 1:
                    Controller_Class.input_data(self)
                elif menu == 2:
                    Controller_Class.print_data(self)
                elif menu == 3:
                    Controller_Class.modify_data(self)
                elif menu == 4:
                    Controller_Class.delete_data(self)
                elif menu == 5:
                    print("종료")
                    break
            except ValueError:
                V.wrong_input_number()
                continue
            except KeyboardInterrupt:
                print("Ctrl + C")

self=()
Controller_Class.run(self)