#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def push(self, node, output):
        if not node:
            return

        self.push(node.left, output)

        output.append(node.val)

        self.push(node.right, output)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        self.push(root, output)
        return output