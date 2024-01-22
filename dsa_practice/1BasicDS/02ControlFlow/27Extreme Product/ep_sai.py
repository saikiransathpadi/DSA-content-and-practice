min_val = float("inf")
max_val = 0

for _ in range(int(input())):
    a = int(input())
    min_val = min(min_val, a)
    max_val = max(max_val, a)

print(min_val * max_val)