class HeadStore:
    def price(self):
        self.store = "본점"
        self.black = 7000
        self.red = 8000
        self.meat = 12000
        self.dump = ""
        self.rice = 1000
    
    def list(self):
        print(f"{self.store} 가격표입니다.")
        # 짜장면
        if self.black == 0:
            print("무료입니다.")
        elif self.black == "":
            print("판매하지 않습니다.")
        else:
            print(f"{self.black}원 입니다.")

        # 짬뽕
        if self.red == 0:
            print("무료입니다.")
        elif self.red == "":
            print("판매하지 않습니다.")
        else:
            print(f"{self.red}원 입니다.")

        # 탕수육
        if self.meat == 0:
            print("무료입니다.")
        elif self.meat == "":
            print("판매하지 않습니다.")
        else:
            print(f"{self.meat}원 입니다.")
        
        # 군만두
        if self.dump == 0:
            print("무료입니다.")
        elif self.dump == "":
            print("판매하지 않습니다.")
        else:
            print(f"{self.dump}원 입니다.")
        
        # 공깃밥
        if self.rice == 0:
            print("무료입니다.")
        elif self.rice == "":
            print("판매하지 않습니다.")
        else:
            print(f"{self.rice}원 입니다.")
        print("================================")

class Store1(HeadStore):
    def price(self):
        self.store = "1호점"
        self.black = 7000
        self.red = 8000
        self.meat = 12000
        self.dump = ""
        self.rice = 1000

class Store2(HeadStore):
    def price(self):
        self.store = "2호점"
        self.black = 5000
        self.red = 5000
        self.meat = 10000
        self.dump = 3000
        self.rice = 0

class Store3(HeadStore):
    def price(self):
        self.store = "3호점"
        self.black = 7000
        self.red = 7000
        self.meat = 12000
        self.dump = 3000
        self.rice = 1000

store1 = Store1()
store1.price()
store1.list()

store2 = Store2()
store2.price()
store2.list()

store3 = Store3()
store3.price()
store3.list()