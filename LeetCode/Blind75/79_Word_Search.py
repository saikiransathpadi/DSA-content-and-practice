from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])
        w = len(word)

        def is_valid(i, j):
            return (
                i >= 0 and
                j >= 0 and
                i < r and 
                j < c
            )

        def dfs(curr, visited: set, i, j):
            if curr >= w: return True
            if not is_valid(i, j): return False
            
            directions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for top in directions:
                if is_valid(*top) and top not in visited and board[top[0]][top[1]] == word[curr]:
                    visited.add(top)
                    if dfs(curr + 1, visited, *top):
                        return True
                    visited.remove(top)
            return False

        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    if dfs(1, set([(i, j)]), i, j):
                        return True
        return False
    


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(Solution().exist(board, word))