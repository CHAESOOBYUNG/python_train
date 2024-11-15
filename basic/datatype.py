# 숫자형
a = 3
b = 8
x = a * b
y = a + b
z = a ** b

print(x)
print(y)
print(z)

# 문자형
print("I ate {0} apples".format(3))

number = 3
print("I eat {0} apples".format(number))

# 문자수 세기
a = "hobby"
a1 = a.count('b')
print(a1)

# 문자 삽입
b = ",".join('abcd')
print(b)
print()

# 위치 알려 주기1: find
a = "python is the best choice"
a1 = a.find('b')
print(a1)
# 14 - 문자열 b가 처음 나온 위치

a2 = a.find('k')
print(a2)
# -1 - 아무것도 없음(false == -1)
print()

# 위치 알려 주기2: index
a = "Life is too short"
a1 = a.index('t')
print(a1)

# a2 = a.index('k')
# print(a2)
# Traceback (most recent call last):
#   File "c:\python_program\datatype.py", line 44, in <module>
#     a2 = a.index('k')
#          ^^^^^^^^^^^^
# ValueError: substring not found 
# -> k가 없으므로 오류 발생
print()

# 소문자 -> 대문자
a = "hi"
a1 = a.upper()
print(a1)

# 대문자 -> 소문자
a= "HI"
a2 = a.lower()
print(a2)

# 왼쪽 공백 지우기
a = " hi "
a1 = a.lstrip()
print(a1)

# 오른쪽 공백 지우기
a = " hi "
a2 = a.rstrip()
print(a2)
print()

# 양쪽 공백 지우기
a = " hi "
a1 = a.strip()
print(a1)

# 문자열 바꾸기: replace
a = "Life is too short"
a2 = a.replace("Life", "Your leg")
print(a1)

# 문자열 나누기: split
a = "Life is too short"
a1 = a.split() # 공백 기준으로 나누기
print(a1)

b = "a:b:c:d"
b1 = b.split(":") # :를 기준으로 나누기
print(b1)
print()

# 사용자로부터 이름 입력받기
name = input("이름을 입력하세요:")

# 입력한 이름 출력
print(f"안녕하세요! {name}님")

# 문자열을 정수로 변환
age = int(input("나이를 입력하세요:"))
print(f"{name}님의 나이는 {age}입니다.")

# <class 'int'>
print(type(age))