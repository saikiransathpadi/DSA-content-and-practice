# L for Lower
# M for Middle
# U for Upper
# SL for Side Lower
# SU for Side Upper
# Invalid for invalid berth number

berths_map = {
    1: "L",
    2: "M",
    3: "U",
    4: "L",
    5: "M",
    6: "U",
    7: "SL",
    0: "SU"
}

for i in range(int(input())):
    c, b = map(int, input().split())
    if b > c:
        print("Invalid")
    else:
        print(berths_map[b % 8])