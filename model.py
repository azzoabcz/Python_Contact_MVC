import cx_Oracle as cxo
from dto import Dto_Class
D = Dto_Class()

class Model_Class():
    # D = Dto_Class()
    # def __init__(self):
    #     self._USER = 'ora_user'
    #     self._PASSWORD = '1234'
    #     self._HOST = 'localhost:1521'
    #     self._SID = 'xe'

    def contact_print(self):
        D = Dto_Class()
        sql = """SELECT a.name_id, a.name, a.phone, a.email, d.div_name
                   FROM allc a
                   JOIN div d
                     ON a.div_num = d.div_num"""
        data = self.print_all(sql)
        list = [Dto_Class(row[0],row[1],row[2],row[3],row[4]) for row in data]
        return list

    def print_one(self, sql):
        conn = cxo.connect('ora_user/1234@localhost:1521/xe')
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        return data

    def print_all(self, sql):
        conn = cxo.connect('ora_user/1234@localhost:1521/xe')
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    def dmi(sql,data):
        conn = cxo.connect('ora_user/1234@localhost:1521/xe')
        cursor = conn.cursor()
        cursor.execute(sql,data)
        cursor.close()
        conn.commit()
        conn.close()

    def dmi_sql(self, sql):
        conn = cxo.connect('ora_user/1234@localhost:1521/xe')
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()

    def add_contact_id(self):
        D = Dto_Class()
        sql_allc_show = 'SELECT MAX(name_id) FROM allc'
        D.get_name_id = self.print_one(sql_allc_show)[0] #0번째 가져오기
        name_id = D.get_name_id+1 if D.get_name_id else 1  #0번째열 최대값 +1
        return name_id

    def add_contact_group_id(self,dto):
        D = Dto_Class()
        division = dto.get_division()
        sql_div_match = f"SELECT div_num FROM div WHERE div_name = '{division}'"
        divnums = self.print_one(sql_div_match)

        if divnums:
            divnums=divnums[0]
            return divnums
        else:
            sql_div_num_add = 'SELECT MAX(div_num) FROM div'
            div_id = self.print_one(sql_div_num_add)[0]
            divnums = div_id+1
            sql_div_name_add = 'INSERT INTO div VALUES(:1,:2)'
            sql_div_input_data = (divnums, f'{division}')
            Model_Class.dmi(sql_div_name_add,sql_div_input_data)
            return divnums

    def add_contact(self,dto):
        D = Dto_Class()
        name_id = self.add_contact_id()
        name = dto.get_name()
        phone = dto.get_phone()
        email = dto.get_email()
        division = Model_Class.add_contact_group_id(self,dto)
        sql_allc_input_data = 'INSERT INTO allc VALUES(:1,:2,:3,:4,:5)'
        sql_div_input_data = (name_id, name, phone, email, division)
        Model_Class.dmi(sql_allc_input_data,sql_div_input_data)

    def delete_contact(self,dto):
        input_name = dto.get_name()
        sql = f"select a.name_id, a.name, a.phone, a.email, d.div_name " \
              f"from allc a, div d " \
              f"where a.div_num = d.div_num " \
              f"and a.name = '{input_name}'"
        data = self.print_all(sql)
        del_list = [Dto_Class(row[0], row[1], row[2], row[3], row[4]) for row in data]
        return del_list

    def delete_model(self,dto):
        input_id = dto.get_id()
        sql = f"delete from allc where name_id = '{input_id}'"
        self.dmi_sql(sql)
