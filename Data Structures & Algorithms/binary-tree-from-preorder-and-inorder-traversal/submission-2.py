class Solution:
    def buildTree(self, preorder, inorder):
        inorderMap = {}

        for i, n in enumerate(inorder):
            inorderMap[n] = i

        preorderIndex = 0

        def dfs(left, right):
            nonlocal preorderIndex

            if left > right:
                return None

            rootVal = preorder[preorderIndex]
            preorderIndex += 1

            root = TreeNode(rootVal)

            mid = inorderMap[rootVal]

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)