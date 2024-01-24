ans = "false"
prev = None

for i in range(int(input())):
    next = int(input())
    if prev and next + prev > 100:
            ans = "true"
    prev = next

print(ans)