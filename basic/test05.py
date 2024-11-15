a = int(input("정수값:"))
b = True
while b:
    if a > 0:
        if a % 3 == 0:
            print("이 값은 3으로 나누어집니다.")
            break
        elif a % 3 == 1:
            print("이 값을 3으로 나눈 나머지는 1입니다.")
            break
        elif a % 3 == 2:
            print("이 값을 3으로 나눈 나머지는 2입니다.")
            break
    else: 
        print("양수가 아닌 값을 입력했습니다.")
        break

    