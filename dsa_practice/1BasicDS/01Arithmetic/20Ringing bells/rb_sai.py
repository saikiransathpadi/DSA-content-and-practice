input()

bell_mins = list(map(int, input().split()))

i = max(bell_mins)

while True:
    if all([i % j == 0 for j in bell_mins]):
        print(i)
        break
    i += 1