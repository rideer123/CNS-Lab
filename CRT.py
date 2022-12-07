def inv(a, m):
    m0 = m
    x0 = 0
    x1 = 1

    if (m == 1):
        return 0

    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t

    if (x1 < 0):
        x1 = x1 + m0

    return x1


def findMinX(num, rem, k):
    prod = 1
    for i in range(0, k):
        prod = prod * num[i]

    result = 0

    for i in range(0, k):
        pp = prod // num[i]
        result = result + rem[i] * inv(pp, num[i]) * pp

    return result % prod


num = [3,5,7]
rem = [2,3,2]
# x = 129934811447123020117172145698449(mod 25)
# x = 129934811447123020117172145698449(mod 4)
# n = int(input("Enter n: "))
# rem = []

# num = list(map(int, input("Enter nums : ").strip().split()))[:n]
# rem = list(map(int, input("Enter rems : ").strip().split()))[:n]
x=findMinX(num, rem, 3)

print("x(mod n)=r")

print("x is", x)
for i in range(3):
        print(x, "mod",num[i-1],"=",rem[i-1])
