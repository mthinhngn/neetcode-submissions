# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """ 
        Input: root = [1,2,3,4,null,null,null,5]
        Output: [1,3,4,5]

                                    1             <-
                                   / \
                                  2   3 
                                 /
                                4
                               /
                              5
        BFS
        Idea: add the last value from the queue at each level to the res
        
        root = [1,2,3,null,4,null,5]
        [1]
        [2,3]
        [null,4,null,5]
        res = [1,3,5]

        Initiate a queue and add root
        res = []
        
        If not root:
            return res
        
        while q:
            Iterate the q
                pop the node
                check left child
                    append left to q
                check right child
                    append right to q
            append node to res   #this append the last node we pop
        return res
        """ 

        q = collections.deque([root])
        res = []

        if not root:
            return res
        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(node.val)
        return res