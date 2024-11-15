import math

a = 200
b = 80

gcd = math.gcd(a, b)

l = math.sqrt(gcd)

print(f"정사각형 선의 길이: {l:.2f}, 필요한 타일 개수: {gcd}")