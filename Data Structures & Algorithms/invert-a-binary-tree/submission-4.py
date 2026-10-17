# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """ 
        1. Handle the edge case root in None
        2. Swap the children
            Using DFS recursive template
            Using BFS queue template
        """
        if not root:
            return
        
        #Swap the children template
        tmp =  root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

