n = int(input())

num = 0
i = 0
mul = 1

if n < 0:
    mul = -1
    n = n * mul
while n > 0:
    rem = n % 10
    num = (num * (10)) + rem
    i += 1
    n //= 10

print(num * mul)