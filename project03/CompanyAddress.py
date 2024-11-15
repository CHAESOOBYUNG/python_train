from Address import Addr 

class CompanyAddr(Addr):
    def __init__(self, name, phone, email, address, group, birth, company, section, position):
        super().__init__(name, phone, email, address, group)
        self.__birth = birth
        self.__company = company
        self.__section = section
        self.__position = position

    def get_birth(self):
        return self.__birth
    
    def set_birth(self, value):
        self.__birth = value

    def get_company(self):
        return self.__company
    
    def set_company(self, value):
        self.__company = value

    def get_section(self):
        return self.__section
    
    def set_section(self, value):
        self.__section = value

    def get_position(self):
        return self.__position
    
    def set_position(self, value):
        self.__position = value

    def print_info(self):
        super().print_info()
        print(f"생일: {self.get_birth()}")
        print(f"회사 이름: {self.get_company()}")
        print(f"부서 이름: {self.get_section()}")
        print(f"직급: {self.get_position()}")