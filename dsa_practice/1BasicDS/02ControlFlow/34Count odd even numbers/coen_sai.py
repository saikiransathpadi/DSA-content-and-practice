even_count = 0
odd_count = 0

for i in range(int(input())):
    ele = int(input())

    if ele % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(odd_count)
print(even_count)

