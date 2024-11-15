a = int(input("정수 A:"))
b = int(input("정수 B:"))

# if a > b:
#     while a != b:
#         print(b)
#         b+=1
#     print(a)
# elif b > a:
#     while a != b:
#         print(a)
#         a+=1
#     print(b)

if a > b:
    start = b
    end = a
    while start <= end:
        print(start)
        start += 1
else:
    start = a
    end = b
    while start <= end:
        print(start)
        start += 1