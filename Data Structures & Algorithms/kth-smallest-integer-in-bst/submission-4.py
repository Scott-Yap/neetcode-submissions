# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0

        def traverse(node, k):
            nonlocal count

            if not node:
                return None

            left_result = traverse(node.left, k)
            if left_result is not None:
                return left_result

            count += 1
            if count == k:
                return node.val

            return traverse(node.right, k)

        return traverse(root, k)