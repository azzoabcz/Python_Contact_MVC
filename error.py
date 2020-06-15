import re

def number_error(num):
    # regex = re.compile(r"(^0\d{1,2})\D?(\d{3,4})\D?(\d{4})")
    regex = re.compile(r"(\d\d\d[-]\d\d\d\d[-]\d\d\d\d)")
    m = regex.match(num)
    if m:
        # data = m.group(1) + m.group(2) + m.group(3)
        data = m.group()
        return data
    else:
        raise regex_exception()

def email_error(email):
    regex = re.compile(r"(\w+[@]\w+[.]\w+)")
    m = regex.match(email)
    if m :
        return m.group()
    else:
        raise regex_exception()



class regex_exception(Exception):
    def __str__(self):
        return "똑바로 하세요"






