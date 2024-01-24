import math
def is_prime(n):
    if n == 2:
        return "Yes"
    for i in range(2, int(math.sqrt(n)) +1):
        if n % i == 0:
            return "No"
    return "Yes"

for _ in range(int(input())):
    print(is_prime(int(input())))
