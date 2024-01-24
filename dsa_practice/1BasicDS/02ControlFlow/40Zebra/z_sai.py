is_zebra = True

prev = None

for i in range(int(input())):
    curr = int(input())
    if prev:
        # print(prev, curr)
        if (prev >=0 and curr < 0) or (curr >=0 and prev < 0):
            pass
        else:
            is_zebra = False
    prev = curr

print(is_zebra)