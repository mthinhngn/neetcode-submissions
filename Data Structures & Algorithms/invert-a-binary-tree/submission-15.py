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
            - self.intertTree(invert the root left child)
            - self.invertTree(invert the root right child)
            
            Using BFS queue template
            - Create a queue = collections.deque([root]) and assign the root
            - While q is not empty
                - pop the node from queue
                - assign node left child = node right child
                - assign node right child= node left child
                - If node.left child is True
                    add node left child to queue
                - If node.left child is True
                    add node right child to queue
                
        """
        if not root:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root