list1 = [1, -2, 3, -5, 8, -3]
a = filter(lambda x: x >= 0, list1)
a = list(a)
print(a)