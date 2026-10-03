# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])

        while queue:
            node1, node2 = queue.popleft()

            # both are None -> this position matches
            if not node1 and not node2:
                continue

            # one is None, the other is not
            if not node1 or not node2:
                return False

            # values are different
            if node1.val != node2.val:
                return False

            # compare corresponding children later
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))

        return True