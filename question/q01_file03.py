# 파일의 문자열로 바꾸기
f = open("C:\\Users\\user\\Desktop\\python\\question\\test.txt", 'r')
body = f.read()
f.close()
body = body.replace("java", "python")
f = open("C:\\Users\\user\\Desktop\\python\\question\\test.txt", 'w')
f.write(body)
f.close()