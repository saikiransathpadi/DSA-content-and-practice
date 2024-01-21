a = int(input())

while a > 0:
    if a % 2 == 0:
        a-= 11
    else:
        a -= 21
print(a)