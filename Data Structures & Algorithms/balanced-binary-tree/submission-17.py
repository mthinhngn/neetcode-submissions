# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = 0
        def dfs(root):
            if not root:
                return True
            
            nonlocal res
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, abs(left-right))
            return 1 + max(left, right)
        dfs(root)
        return res <= 1