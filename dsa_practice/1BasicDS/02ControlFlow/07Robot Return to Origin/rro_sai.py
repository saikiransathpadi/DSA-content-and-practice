class Solution:
    def judgeCircle(self, moves: str) -> bool:
        start = [0,0]
        for i in moves:
            if i == "R":
                start [0] +=1
            elif i == "L":
                start [0] -= 1
            elif i == "U":
                start[1] += 1
            elif i == "D":
                start[1] -= 1
        if start == [0, 0]:
            return True
        return False