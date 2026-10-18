# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Input: root = [1,2,3,4,5,6,7]
        Output: [[1],[2,3],[4,5,6,7]]

                            1
                           / \
                          2   3
                         /\   /\
                        4  5 6  7  
        BFS queue
        If not root:
            return
        
        Create a queue, add to root
        res = []

        while q:
            for i in range(len(q))
                Pop the node
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append([node])
        return res
        """
        
        q = collections.deque([root])
        res = []

        if not root:
            return res
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res