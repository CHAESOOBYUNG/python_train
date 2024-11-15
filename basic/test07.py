a = int(input("정수 a:"))
b = int(input("정수 b:"))

# if a >= b:
#     print("a >= b가 되도록 정렬했습니다.")
#     print(f"변수 a는 {a}입니다.")
#     print(f"변수 b는 {b}입니다.")
# else:
#     print("a >= b가 되도록 정렬했습니다.")
#     print(f"변수 a는 {b}입니다.")
#     print(f"변수 b는 {a}입니다.")

c = [a, b]
c.sort(reverse=True)
print("a >= b가 되도록 정렬했습니다.")
print(f"변수 a는 {c[0]}입니다.")
print(f"변수 b는 {c[1]}입니다.")
