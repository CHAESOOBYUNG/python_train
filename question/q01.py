# 홀수, 짝수 판별하기
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
         return False

# 모든 입력의 평균값 구하기
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result

print(avg_numbers(1, 2))
print(avg_numbers(1, 2, 3, 4, 5))

# 프로그램 오류 수정하기 1
input1 = int(input("첫 번째 숫자를 입력하세요: "))
input2 = int(input("두 번째 숫자를 입력하세요: "))
total = input1 + input2
print("두 수의 합은 %s입니다" % total)

# 출력 결과가 다른 하나
print("you" "need" "python")
print("you" + "need" + "python")
print("you", "need", "python") # 다른 하나
print("".join(["you" "need" "python"]))