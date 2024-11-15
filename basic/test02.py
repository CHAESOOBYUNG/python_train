# a = input("정수값:")
# b = len(a)

# print(f"1 ~ 마지막 2번째 숫자는 {a[0:b-1]}입니다.")
# print(f"마지막 숫자는 {a[b-1]}입니다.")

a = int(input("정수값:"))

print(f"1 ~ 마지막 2번째 숫자는 {int(a / 10)}입니다.")
print(f"마지막 숫자는 {a % 10}입니다.")