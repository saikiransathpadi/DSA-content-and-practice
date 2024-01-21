import math



max_que, tests = map(int, input().split())

primes = [1, *[i for i in range(2, max_que+1)]]

i = 1

while i < len(primes):
    if primes[i] != -1:
        k = 2
        j = primes[i] * k
        while j < len(primes)+1:
            primes[j-1] = -1
            j = primes[i] * k
            k+=1
    i += 1


def find_low_count(arr, num):
    count = 0
    for i in arr:
        if i !=1 and i!= -1 and i <= num:
            count += 1
        elif i > num:
            return count
    return count


for i in range(tests):
    count = 0
    print(find_low_count(primes, int(input())))
