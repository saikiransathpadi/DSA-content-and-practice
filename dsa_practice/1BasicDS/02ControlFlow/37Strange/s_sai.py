# your code goes here

count = 0

for i in range(int(input())):
    ele = int(input())
    digit_sum = 0
    digit_prod = 1
    if ele == 0:
        count += 1
    while ele:
        last_digit = ele % 10
        digit_prod *= last_digit
        digit_sum += last_digit
        ele = ele // 10
    if digit_sum >= digit_prod:
        count += 1
print(count)
