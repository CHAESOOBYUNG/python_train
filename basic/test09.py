num = int(input("몇 월인가요?"))

if num >= 3 and num <= 5:
    print("봄")
elif num >= 6 and num <= 8:
    print("여름") 
elif num >= 9 and num <= 11:
    print("가을")
elif num == 1 or num == 2 or num == 12:
    print("겨울")
else:
    print("그런 월은 없습니다.") 