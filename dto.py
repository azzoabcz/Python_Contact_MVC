class Dto_Class:

    def __init__(self,
                 name_id = 0,
                 name = "",
                 phone = "",
                 email = "",
                 division = ""):
        self._name_id = name_id
        self._name = name
        self._phone = phone
        self._email = email
        self._division = division

    def get_id(self):
        return self._name_id
    def set_id(self,name_id):
        self._name_id =name_id

    def get_name(self):
        return self._name
    def set_name(self,name):
        self._name = name

    def get_phone(self):
        return self._phone
    def set_phone(self, phone):
        self._phone = phone

    def get_email(self):
        return self._email
    def set_email(self, email):
        self._email = email

    def get_division(self):
        return self._division
    def set_division(self,division):
        self._division = division


