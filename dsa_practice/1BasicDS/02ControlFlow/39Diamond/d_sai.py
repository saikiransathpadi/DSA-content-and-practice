n = int(input())

spaces = n-1
stars = 1

for i in range(n):
    print(" "*spaces + "*"*stars)
    spaces -= 1
    stars += 2

spaces = 1
stars = stars - 4

for i in range(n-1):
    print(" "*spaces + "*"*stars)
    spaces += 1
    stars -= 2