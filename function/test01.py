def checkVaccin():
    age = year - birthyear
    result = ""
    if age <= 12 or age >= 59:
        result = "무료 예방접종이 가능합니다."
    else:
        result = "무료 접종 대상이 아닙니다."
    return result

def healthCheck():
    age = year - birthyear
    result = ""
    if age >= 18 and age % 2 == 0:
        result = "무료 건강검진 대상입니다."
    elif year % 2 == birthyear:
        result = "무료 건강검진 대상입니다."
    elif age >= 39:
        result = "무료 건강검진 대상입니다.\n암 검사도 무료입니다."
    else:
        result = "무료 건강검진 대상이 아닙니다."
    return result

         

birthyear = int(input("태어난 해를 입력하세요."))
year = int(input("올해 년도를 입력하세요."))
print(checkVaccin())
print(healthCheck())
