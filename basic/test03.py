# num = int(input("정수값:"))
# if num > 0:
#     print(f"절대값은 {num}입니다.")
# else:
#     print(f"절대값은 {-num}입니다.")

num = int(input("정수값:"))
while True:
    if num > 0:
        print(f"절대값은 {num}입니다.")
        break
    elif num == 0:
        print(f"절대값은 {num}입니다.")
        break
    else:
        print(f"절대값은 {-num}입니다.")
        break
        