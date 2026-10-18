# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Input: root = [2,1,1,3,null,1,5]
        Output: 3, [2,3,5]

                                2  <-
                               / \
                              1   1
                             /   / \
                        ->  3   1   5  <-

        DFS. Compare current node with maxPrev 


        (node,prevMax)
        (2,0)  -> pM = 2 (G)
        left
        (1,2)  -> pM = 2
        (3,2)  -> pM = 3 (G)

        right
        (1,2)  -> pM = 2
        (5,2)  -> pM = 5 (G)
        
        res = 0
        If not root:
            return res
        
        Def dfs(node, prevMax)
            nonlocal res
            if not node:
                return res
            
            if node.val >= prevMax val:
                res += 1

            #Update the prevMax 
            prevMax = max(node.val, prevMax)
            
            res += dfs(node.left, prevMax)
            res += dfs(node.right, prevMax)
        
        Calling dfs(root, root.val)
        return res
        """

        res = 0
        if not root:
            return res
        
        def dfs(node, prevMax):
            nonlocal res

            if not node:
                return
            
            if node.val >= prevMax:
                res += 1
            
            prevMax = max(node.val, prevMax)
            dfs(node.left, prevMax)
            dfs(node.right, prevMax)
        
        dfs(root,root.val)
        return res