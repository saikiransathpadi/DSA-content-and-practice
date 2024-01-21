for i in range(int(input())):
    inp = input()
    if len(inp) % 15 == 0:
        print("foobar")
    elif len(inp) % 3 == 0:
        print("foo")
    elif len(inp) % 5 == 0 :
        print("bar")
    else:
        print("-")