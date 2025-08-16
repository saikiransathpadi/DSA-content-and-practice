from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root: return True
        
        def isValidNodeLeft(root, tree):
            if not tree: return True

            if tree.val >= root.val: return False

            return isValidNodeLeft(root, tree.left)and isValidNodeLeft(root, tree.right)
        
        def isValidNodeRight(root, tree):
            if not tree: return True

            if tree.val <= root.val: return False

            return isValidNodeRight(root, tree.left)and isValidNodeRight(root, tree.right)
        
        if isValidNodeLeft(root, root.left) and isValidNodeRight(root, root.right):
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        
        return False


