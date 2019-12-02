"""
Given a binary tree, return the preorder traversal of its nodes' values.
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return "TreeNode(%s, %s, %s)"%(self.val, self.left, self.right)

class Solution:
    def preorderTraversal(self, root: TreeNode, val=None) -> List[int]:
        if val is None:
            val = []
        if root and root.val:
            val.append(root.val)
        if root and root.left:
            self.preorderTraversal(root.left, val)
        if root and root.right:
            self.preorderTraversal(root.right, val)
        return val
if __name__=="__main__":
    root = TreeNode(1)
    root.left = None
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    t = Solution()
    t.preorderTraversal(root)
    print(t)

