# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):

            #base case 
            if not node:
                return 0, True  

            height_left, left_ok = height(node.left)

            height_right, right_ok = height(node.right)

            diff = abs(height_left - height_right)

            balanced = left_ok and right_ok and diff <= 1
                
            return 1 + max(height_left, height_right), balanced

        return height(root)[1]