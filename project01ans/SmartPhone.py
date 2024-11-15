# SmartPhone.py의 파일

from Address import Addr # Addr 클래스를 사용하기위해 임포트

class SmartPhone:
    def __init__(self):
        self.contacts = [] # 최대 10개의 연락처를 저장할 리스트

    def input_addr_data(self): # 입력
        # 사용자로부터 연락처 데이터를 입력받음
        name = input("이름을 입력하세요: ")
        phone = input("전화번호를 입력하세요: ")
        email = input("이메일을 입력하세요: ")
        address = input("주소를 입력하세요: ")
        group = input("그룹(친구/가족)을 입력하세요: ")

        return Addr(name, phone, email, address, group) # 주소값 리턴
    
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