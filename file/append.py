f = open("C://Users//user//Desktop//python//file//new1.txt", "a")
for i in range(11, 20):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()
