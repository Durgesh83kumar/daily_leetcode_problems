# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        ans = []
        
        def pathSum(node, path):
            if node is None:
                return
            if path:
                path += "->" + str(node.val)
            else:
                path += str(node.val)
            if node.left is None and node.right is None:
                ans.append(path)
                return
            pathSum(node.left, path)
            pathSum(node.right, path)

        pathSum(root, "")
        return ans