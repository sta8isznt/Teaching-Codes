# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:  # Both trees are empty
            return True
        if not p or not q or p.val != q.val:  # One tree is empty or values don't match
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        