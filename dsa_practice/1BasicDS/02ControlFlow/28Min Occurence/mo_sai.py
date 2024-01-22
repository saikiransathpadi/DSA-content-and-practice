num = None
count = 0

for i in range(int(input())):
    if i == 0:
        num = int(input())
        count = 1
    else:
        if int(input()) == num:
            count += 1
    
print(count)