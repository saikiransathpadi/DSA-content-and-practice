n = int(input())

spaces = n-1
stars = 1

for i in range(n):
    if i % 2 ==0:
        pattern = "*$"
    else:
        pattern = "$*"
    print(" "*spaces + (pattern*stars)[:stars])
    spaces -= 1
    stars += 2
