

n,i = map(int, input().split())

if n % 2 == 1 and (n//2) + 1 == i:
    print(i)
else:
    print(n-i+1)