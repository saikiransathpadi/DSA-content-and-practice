for i in range(int(input())):
    a,b = map(int, input().split())
    if b > a:
        a,b = b,a
    
    while True:
        if a % b ==0:
            print(b)
            break
        else:
            a,b = b, a%b
