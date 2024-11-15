class Addr:
    def __init__(self, name, phone, email, address, group):
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__address = address
        self.__group = group
    
    # name의 getter(속성값 읽기)와 setter(속성값 변경)
    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value
    
    # phone의 getter와 setter
    def get_phone(self):
        return self.__phone
    
    def set_phone(self, value):
        self.__phone = value

    # email의 getter
    def get_email(self):
        return self.__email
    
    # address의 getter
    def get_address(self):
        return self.__address
    
    # group의 getter
    def get_group(self):
        return self.__group
    
    # 정보 출력 메서드
    def print_info(self):
        print(f"이름: {self.get_name()}")
        print(f"전화번호: {self.get_phone()}")
        print(f"이메일: {self.get_email()}")
        print(f"주소: {self.get_address()}")
        print(f"그룹(친구/가족): {self.get_group()}") 