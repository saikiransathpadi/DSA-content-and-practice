ordered, not_eaten = map(int, input().split())

items_prices = list(map(int, input().split()))

charged = int(input())

ans = (int(charged - ((sum(items_prices) - items_prices[not_eaten])/2)))

if ans == 0:
    print("It is Correct!")
else:
    print(ans)
