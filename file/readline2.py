f = open("C://Users//user//Desktop//python//file//new1.txt")
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()