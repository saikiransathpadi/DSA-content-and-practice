sum = 0

for i in range(int(input())):
    if i %2 ==0:
        sum += int(input())
    else:
        sum -= int(input())

print(sum)