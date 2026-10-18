# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4
                            5
                           / \
                          3   8
                         /\   /\
                        1  4 7  9
                         \ 
                          2 

        Because this is the binary binary search tree:
        left child < root < right child

        We will compare the value of the p and q to the node we at
            if p.val and qval > node
                go right
            if p.val and qval < node
                go left
            
            #either mean q.val > node and p.val < node, 
            q.val < node and   p.val > node
            the current node is has happend to be LCA
            ex: p = 2, q = 4
            2 < 5 and 4 < 5. Go right
            2 < 3 and 4 > 3. 3 is the LCA
        """
        node = root

        while node:
            if p.val > node.val and q.val > node.val:
                node = node.right
            elif p.val < node.val and q.val < node.val:
                node = node.left
            else:
                return node