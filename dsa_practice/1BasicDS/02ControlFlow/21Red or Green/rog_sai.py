s = input()

r_count = 0
g_count = 0

for i in s:
    if i =="R":
        r_count += 1
    else:
        g_count += 1
print(min(r_count, g_count))