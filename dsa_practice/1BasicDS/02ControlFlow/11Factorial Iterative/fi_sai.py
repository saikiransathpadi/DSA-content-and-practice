a = int(input())

fac = 1

if a < 0:
    print("undefined")
else:
    for i in range(1, a+1):
        fac *=i
    print(fac)