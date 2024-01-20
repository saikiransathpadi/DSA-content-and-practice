# your code goes here

a,b = map(int, input().split())

sum = a+b

if sum <= 12:
    print(sum)
else:
    print (((a+b) % 12) or 12)