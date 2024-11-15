f = open("C://Users//user//Desktop//python//file//new1.txt", "w")
for i in range(1, 11):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()