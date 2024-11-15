from Address import Addr

class CustomerAddr(Addr):
    def __init__(self, name, phone, email, address, group, birth, customer, item, position):
        super().__init__(name, phone, email, address, group)
        self.__birth = birth
        self.__customer = customer
        self.__item = item
        self.__position = position

    def get_birth(self):
        return self.__birth
    
    def set_birth(self, value):
        self.__birth = value

    def get_customer(self):
        return self.__customer
    
    def set_customer(self, value):
        self.__customer = value

    def get_item(self):
        return self.__item
    
    def set_item(self, value):
        self.__item = value

    def get_position(self):
        return self.__position
    
    def set_position(self, value):
        self.__position = value

    def print_info(self):
        super().print_info()
        print(f"생일: {self.get_birth()}")
        print(f"거래처 이름: {self.get_customer()}")
        print(f"품목 이름: {self.get_item()}")
        print(f"직급: {self.get_position()}")