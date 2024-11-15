import Address

# 주소록을 저장할 리스트
address = []

def save(): # 저장
    name = input("이름: ")
    phonenumber = input("전화번호: ")
    email = input("이메일: ")
    address_input = input("주소: ")
    group = input("그룹(친구/가족): ")
    
    # Address 객체 생성 후 리스트에 추가
    new_entry = Address.Addr(name, phonenumber, email, address_input, group)
    address.append(new_entry)
    print("저장이 완료되었습니다.")

def update(): # 수정
    name_update = input("수정할 이름을 입력하세요: ")
    for entry in address:
        if entry.name == name_update:
            inform = True # 수정할 정보 while문 다룸
            while inform:
                print("1. 전화번호 2. 이메일 3. 주소 4. 그룹 5. 나가기")
                new_inform = input("수정할 정보(번호)를 입력하세요: ")
                if new_inform == "1":
                    entry.phonenumber = input(f"{name_update}의 새로운 전화번호: ")
                    print(f"{name_update}의 전화번호가 수정되었습니다.")
                elif new_inform == "2":
                    entry.email = input(f"{name_update}의 새로운 이메일: ")
                    print(f"{name_update}의 이메일이 수정되었습니다.")
                elif new_inform == "3":
                    entry.address = input(f"{name_update}의 새로운 주소: ")
                    print(f"{name_update}의 주소가 수정되었습니다.")
                elif new_inform == "4":
                    entry.group = input(f"{name_update}의 새로운 그룹: ")
                    print(f"{name_update}의 그룹이 수정되었습니다.")
                elif new_inform == "5":
                    inform = False
                else:
                    print("1~5 사이의 정수를 입력해주세요.")
        else:
            print(f"{name_update}의 정보가 존재하지 않습니다.")
        return
        

def delete(): # 삭제
    name_delete = input("삭제할 이름을 입력하세요: ")
    for entry in address:
        if entry.name == name_delete:
            address.remove(entry)
            print(f"{name_delete}의 정보가 삭제되었습니다.")
            return
    print(f"{name_delete}의 정보가 존재하지 않습니다.")

def select(): # 출력
    if not address:
        print("주소록에 저장된 정보가 없습니다.")
        return
    
    print("주소록 정보:")
    for entry in address:
        print(entry)
        print()

def search(): # 검색
    name_search = input("검색할 이름을 입력하세요: ")
    for entry in address:
        if entry.name == name_search:
            print(entry)
        else:
            print("검색 결과가 없습니다.")
        
    