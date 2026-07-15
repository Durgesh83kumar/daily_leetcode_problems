# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if(p is None and q is None):
            return True
        # elif((p is None and q is not None) or (p is not None and q is None)):
        if(p is None or q is None):
            return False
        # elif(p is not None and q is None):
        #     return False
        # else:
        #     if(p.val != q.val):
        #         return False
            
        #     left = self.isSameTree(p.left, q.left)
        #     right = self.isSameTree(p.right, q.right)

        if(p.val != q.val):
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        # if(left == True and right == True):
        #     return True
        # else:
        #     return False
        return left and right