# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def helper(self, root):
        if(root is None):
            return 0, True
        
        l_h, l_b = self.helper(root.left)
        r_h, r_b = self.helper(root.right)

        current_height = 1 + max(l_h,r_h)
        current_balanced = l_b and r_b and abs(l_h - r_h)<=1

        return current_height , current_balanced
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        current_height, current_balanced = self.helper(root)
        return current_balanced