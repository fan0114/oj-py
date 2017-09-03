# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left is not None and root.right is not None:
            if root.left.val>root.val:
                leftMin=root.left.val
            else:
                leftMin = self.findSecondMinimumValue(root.left)
            if root.right.val>root.val:
                rightMin=root.right.val
            else:
                rightMin = self.findSecondMinimumValue(root.right)
            if leftMin>=0 and (leftMin<=rightMin or rightMin<0):
                return leftMin
            elif rightMin>=0 and (rightMin<=leftMin or leftMin<0):
                return rightMin
        return -1