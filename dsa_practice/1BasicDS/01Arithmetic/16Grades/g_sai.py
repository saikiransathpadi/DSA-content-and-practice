for i in range(int(input())):
    marks = int(input())
    if marks < 38:
        print(marks)
    else:
        remainder = marks % 5
        if remainder >= 3:
            print(marks + (5 - remainder))
        else:
            print(marks)