# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lower=float('-inf'), upper=float('inf')):
            if not root:
                return True

            curr = root.val

            # Check if the current node's value is within the valid range
            if not (lower < curr < upper):
                return False

            # Check the left subtree with updated upper limit
            # Check the right subtree with updated lower limit
            return (
                dfs(root.left, lower, curr) and
                dfs(root.right, curr, upper)
            )

        return dfs(root)
