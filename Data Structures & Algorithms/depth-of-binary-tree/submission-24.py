# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
                 1
                / \
               2   3
                  /
                 4
        
        q = [1]
        process[1], 1 has left(2) and right(3)      
        q.append(root.left) and root.right
        
        q = [2,3]
        prcosses[2], no left no right
        q = [3]
        processes[3], left(4)
        q.append(root.left)

        q = [4], no left no right
        q = [] -> out while loop
        """
        if not root:
            return 0
      

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    