# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
                 1
                / \
               2   3
                  /
                 4
        dfs(2):
        left = 0
        right = 0
        res = max(0,0) = 0

        dfs(4):
        left = 0
        right =0
        res = 0

        dfs(3)
        left=1
        right=0
        res =1

        dfs(1)
        left =0
        right =1
        res = 1
        
        """
        res =0
        def dfs(root):
            if not root:
                return True
            nonlocal res
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, abs(left-right))
            return 1 + max(left,right)
        dfs(root)
        return res <=1