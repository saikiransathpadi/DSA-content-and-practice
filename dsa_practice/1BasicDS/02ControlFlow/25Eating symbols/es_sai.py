s = input()

sum = 0

for i in s:
    if i =="-":
        sum -= 1
    else:
        sum += 1
print(sum)
