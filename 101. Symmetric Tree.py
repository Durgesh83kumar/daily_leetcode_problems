# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True
        
        def isMirror(left, right):
            if(left is None and right is None):
                return True
            if(left is None or right is None):
                return False
            if(left.val != right.val):
                return False
            mirror1 = isMirror(left.left, right.right)
            mirror2 = isMirror(left.right, right.left)

            return mirror1 and mirror2

        return isMirror(root.left, root.right)