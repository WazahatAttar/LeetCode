# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.pred = -float('inf')
        def recur(node):
            if not node:
                return True
            if not recur(node.left):
                return False
            if self.pred >= node.val:
                return False
            self.pred = node.val
            if not recur(node.right):
                return False
            return True
        return recur(root)