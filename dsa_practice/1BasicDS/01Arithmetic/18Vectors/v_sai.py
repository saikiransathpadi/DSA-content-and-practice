

a1,a2,a3 = map(int, input().split())
b1,b2,b3 = map(int, input().split())

dot_product = a1 * b1 + a2 * b2 + a3 * b3


cross_product = (a2 * b3 - a3 * b2) ** 2 + (a1 * b3 - b1 * a3)**2 + (a1 * b2 - a2 * b1) ** 2

if cross_product == 0:
    print(1)
elif dot_product == 0:
    print(2)
else:
    print(0)