num = int(input("몇 개의 *를 표시할까요?"))
i = 1
while i <= num:
    if i % 5 != 0:
        print("*", end="") 
    else:
        print("*", end="") 
        print(end="\n")
    i+=1
     