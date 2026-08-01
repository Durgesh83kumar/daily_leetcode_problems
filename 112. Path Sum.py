# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        targetSum -= root.val

        if root.left is None and root.right is None and targetSum == 0:
            return True
        left = self.hasPathSum(root.left,targetSum)
        right = self.hasPathSum(root.right, targetSum)

        return left or right