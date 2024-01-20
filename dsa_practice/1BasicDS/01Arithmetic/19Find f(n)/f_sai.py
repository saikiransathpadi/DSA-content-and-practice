fn = 0

for i in range(int(input())):
    fn += (i+1) * ((-1) ** (i+1))

print(fn)