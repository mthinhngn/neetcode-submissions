# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        return the k smallest value in the tree
        root = [4,3,5,2,null], k = 4
        Output = 5

                                        4
                                       / \
                                      3   5
                                     /
                                    2 

        dfs(4): left → dfs(3)

        dfs(3): left → dfs(2)

        dfs(2): left=None → return | cnt==0? No | cnt 4→3 | cnt==0? No | right=None → return

        dfs(3): left finished      | cnt==0? No | cnt 3→2 | cnt==0? No | right=None → return

        dfs(4): left finished      | cnt==0? No | cnt 2→1 | cnt==0? No | right → dfs(5)

        dfs(5): left=None → return | cnt==0? No | cnt 1→0 | cnt==0? Yes → res=5 → return


        Initiate count, res = k, root.val

        Def dfs(node):
            if node is empty:
                return

            resursion left child 
            if count == 0:
                return
            
            count -= 1
            if count == 0:
                res = node.val
                return
            resursion right child

        dfs(root)
        return res
        """

        count, res =  k, root.val

        def dfs(node):
            nonlocal count, res
            if not node:
                return
            
            dfs(node.left)
            if count == 0:
                return
            count -= 1
            if count == 0:
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res

        