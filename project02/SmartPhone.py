# SmartPhone.py의 파일
from CompanyAddress import CompanyAddr
from CustomerAddress import CustomerAddr

class SmartPhone:
    def __init__(self):
        self.contacts = [] # 최대 10개의 연락처를 저장할 리스트

    def input_company_data(self): # 입력
        # 사용자로부터 연락처 데이터를 입력받음
        print("# 데이터 2개를 입력합니다.")
        name = input("이름: ")
        phone = input("전화번호: ")
        email = input("이메일: ")
        address = input("주소: ")
        group = input("그룹: ")
        birth = input("생일: ")
        company = input("회사 이름: ")
        section = input("부서 이름: ")
        position = input("직급: ")

        return CompanyAddr(name, phone, email, address, group, birth, company, section, position) # 주소값 리턴
    
    def input_customer_data(self): # 입력
        # 사용자로부터 연락처 데이터를 입력받음
        print("# 데이터 2개를 입력합니다.")
        name = input("이름: ")
        phone = input("전화번호: ")
        email = input("이메일: ")
        address = input("주소: ")
        group = input("그룹: ")
        birth = input("생일: ")
        customer = input("거래처 이름: ")
        item = input("품목 이름: ")
        position = input("직급: ")

        return CustomerAddr(name, phone, email, address, group, birth, customer, item, position) # 주소값 리턴

    def add_addr(self, addr): # 저장
        if len(self.contacts) < 10: # 최대 10개의 연락처만 저장
            self.contacts.append(addr)
            print(">>> 데이터가 저장되었습니다.")
        else:
            print("연락처 공간이 가득찼습니다.")

    def print_all_addr(self): # 출력
        if not self.contacts:
            print("저장된 연락처가 없습니다.")
        else: 
            for i, addr in enumerate(self.contacts): # enumerate - range와 같은 기능
                print(f"\n[{i + 1}]")
                addr.print_info()
    
    def search_addr(self, name): # 검색
        for addr in self.contacts:
            if addr.get_name() == name:
                addr.print_info()
                return
        print(f"{name}의 연락처를 찾을 수 없습니다.")

    def delete_addr(self, name): # 삭제
        for addr in self.contacts:
            if addr.get_name() == name:
                self.contacts.remove(addr)
                print(f"{name}의 연락처가 삭제되었습니다.")
                return
        print(f"{name}의 연락처를 찾을 수 없습니다.")

    def edit_addr(self, name, new_addr): # 수정
        for i, addr in enumerate(self.contacts):
            if addr.get_name() == name:
                self.contacts[i] = new_addr
                print(f"{name}의 연락처가 수정되었습니다.")
                return
        print(f"{name}의 연락처를 찾을 수 없습니다.")