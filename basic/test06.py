# a = int(input("정수 a:"))
# b = int(input("정수 b:"))

# if a-b >= 10 or b-a >= 10:
#     print("두 값의 차이는 10이상입니다.")
# else: 
#     print("두 값의 차이는 9이하입니다.")

a = int(input("정수 a:"))
b = int(input("정수 b:"))
if a > b:
    dif = a - b
    if dif >= 10:
        print("두 값의 차이는 10이상입니다.")
    else:
        print("두 값의 차이는 9이하입니다.")
else:
    dif = b - a
    if dif >= 10:
        print("두 값의 차이는 10이상입니다.")
    else:
        print("두 값의 차이는 9이하입니다.")