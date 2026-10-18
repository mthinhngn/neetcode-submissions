# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Input: root = [2,1,3]
        Output: true

                                        2
                                       / \
                                      1   3                         
        DFS
        -inf < root < inf
        Check node.left < node < parent
        CHeck node.right > node > parent

        at 2:
        -inf < 2 < inf

        at 1
        dfs(1, -inf, 2) -> this mean -inf < 1 < 2

        at 3
        dfs(3, 2, inf)  -> this mean 2 < 3 < inf

        calling recursion
        """
        
        def dfs(node, left, right):
            if not node:
                return True
            
            if not (left < node.val < right):
                return False
            
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
        return dfs(root, float("-inf"), float("inf"))