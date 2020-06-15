from dto import Dto_Class
D = Dto_Class

class View_Class:

    def mainmenu(self):
        print("""
        =====================================
            다음 메뉴 중 하나를 선택하세요.
        =====================================
        1. 회원 추가
        2. 회원 목록 보기
        3. 회원 정보 수정하기
        4. 회원 삭제
        5. 종료
        """)
        try:
            menu = int(input(" choose : "))
        except:
            print("숫자(1~5)만 입력하세요")
            menu = int(input(" choose : "))
        return int(menu)


    def input_name(self):
        return input('회원이름을 입력하세요 : ')
    def input_phone(self):
        return input('회원전화번호를 입력하세요(ex:010-1234-1234) : ')
    def input_email(self):
        return input('회원 이메일을 입력하세요(ex:email@domain.com) :')
    def input_divison(self):
        return input('구분를 입력하세요 ')

    def contact_print(self,list):
        print("총 %s명의 회원이 저장 되어 있습니다." %len(list))
        for text in list:
            print(f"이름 :  {text.get_name()},\t"
                  f"전화번호 :  {text.get_phone()},\t"
                  f"이메일 :  {text.get_email()},\t"
                  f"구분 :  {text.get_division()}")

    def contact_delete(self,del_list):
        if not del_list:
            print("일치 하는 이름이 없습니다.")
            return self.mainmenu()
        else:

            for i , text in enumerate(del_list):
                print(f"{i+1}. ,"
                      f"이름 :  {text.get_name()},\t"
                      f"전화번호 :  {text.get_phone()},\t"
                      f"이메일 :  {text.get_email()},\t"
                      f"구분 :  {text.get_division()}")

    def find_index(self):
        return int(input())

    def wrong_input_number(self):
        return print("1 ~ 5 번만 입력하세요")

