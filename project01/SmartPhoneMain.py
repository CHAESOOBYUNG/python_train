import SmartPhone

sp = SmartPhone
onOff = True
while onOff:
    print("\n주소록 관리 프로그램")
    print("1. 연락처 저장")
    print("2. 연락처 수정")
    print("3. 연락처 삭제")
    print("4. 연락처 출력")
    print("5. 연락처 검색")
    print("6. 종료")
    
    choice = input("원하는 작업을 선택하세요: ")
    
    if choice == "1": # 저장
        sp.save()
    elif choice == "2": # 수정
        sp.update()
    elif choice == "3": # 삭제
        sp.delete()
    elif choice == "4": # 출력
        sp.select()
    elif choice == "5": # 검색
        sp.search()
    elif choice == "6": # 종료
        print("프로그램을 종료합니다.")
        onOff = False
    else:
        print("잘못된 입력입니다. 다시 시도하세요.")