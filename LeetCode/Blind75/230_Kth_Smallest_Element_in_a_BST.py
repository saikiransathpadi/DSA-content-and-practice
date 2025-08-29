from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left  
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        i = 0
        
        def dfs(root):
            nonlocal ans, i
            if root:
                dfs(root.left)
                i += 1
                if not ans and i == k:
                    ans = root.val
                dfs(root.right)
        dfs(root)
        return ans