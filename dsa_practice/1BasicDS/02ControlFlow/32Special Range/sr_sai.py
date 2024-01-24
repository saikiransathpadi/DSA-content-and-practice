m = int(input())
n = int(input())

if m < 0 and n < 0:
    print(-1)
else:
    for i in range(max(m, 0), n+1):
        print(i)