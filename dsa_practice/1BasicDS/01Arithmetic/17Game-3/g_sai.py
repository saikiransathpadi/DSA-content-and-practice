for _ in range(int(input())):
    gems = list(map(int, input().split()))
    gems.sort()
    count = gems[1]
    target = gems[2] - count
    # if target % 2 == 1:
    #     target -= 1
    #     count += 1
    while target > 0:
        print(count, target)
        count += 1
        target -= 2
    print(count)
