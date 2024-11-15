from SmartPhone import SmartPhone

class SmartPhoneMain:
    def __init__(self):
        self.smartphone = SmartPhone() # SmartPhone() 생성자 call

    def print_menu(self):
        print("Contact------------------------")
        print("1. 연락처 등록(회사)")
        print("2. 연락처 등록(거래처)")
        print("3. 모든 연락처 출력")
        print("4. 연락처 검색")
        print("5. 연락처 삭제")
        print("6. 연락처 수정")
        print("7. 프로그램 종료")
        print("------------------------")

    def start(self):
        while True:
            self.print_menu()
            choice = input("원하는 작업을 선택하세요 (1-7):")

            if choice == "1": # data 입력
                addr = self.smartphone.input_company_data()
                self.smartphone.add_addr(addr)
            elif choice == "2":
                addr = self.smartphone.input_customer_data()
                self.smartphone.add_addr(addr)
            elif choice == "3":
                self.smartphone.print_all_addr()
            elif choice == "4":
                name = input("검색할 이름을 입력하세요: ")
                self.smartphone.search_addr(name)
            elif choice == "5":
                name = input("삭제할 이름을 입력하세요: ")
                self.smartphone.delete_addr(name)
            elif choice == "6":
                name = input("수정할 이름을 입력하세요: ")
                print("새로운 연락처 정보를 입력하세요.")
                contact_type = input("회사 연락처입니까? (y/n)").strip().lower()
                if contact_type == 'y':
                    new_addr = self.smartphone.input_company_data()
                else:
                    new_addr = self.smartphone.input_customer_data
                self.smartphone.edit_addr(name, new_addr)
            elif choice == "7":
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 다시 선택하세요.")

# 프로그램 실행 부분
if __name__ == "__main__":
    smartphone_main = SmartPhoneMain()
    smartphone_main.start()