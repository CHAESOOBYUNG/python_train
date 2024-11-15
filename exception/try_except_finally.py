file = None

try:
    file = open("sample.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
finally:
    if file:
        file.close()
        print("파일이 닫혔습니다.")
    else:
        print("Do nothing!")