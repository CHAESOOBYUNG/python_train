import random

number = random.randint(0,10)

if number == 0:
    print("가위")
elif number == 1:
    print("바위")
elif number == 2:
    print("보")
else:
    print("가위바위보 수가 아닙니다.")
print(number)