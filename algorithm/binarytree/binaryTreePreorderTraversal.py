"""
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
"""
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return "TreeNode(%s, %s, %s)"%(self.val, self.left, self.right)
class Solution:
    def inorderTraversal(self, root: TreeNode, t=None) -> List[int]:
        if t is None:
            t = []
        if root and root.left:
            self.inorderTraversal(root.left, t)
        if root and root.val:
            t.append(root.val)
        if root and root.right:
            self.inorderTraversal(root.right, t)
        return t
if __name__=="__main__":
    root = TreeNode(1)
    root.left = None
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
     
    print(root)
    t = Solution()
    print(t.inorderTraversal(root))
    

