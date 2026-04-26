# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, max_number):
        if node == None:
            return 0

        count = 0
        if node.val >= max_number:
            count += 1
            max_number = node.val
        
        return count + self.dfs(node.left, max_number) + self.dfs(node.right, max_number)
        
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        if root == None:
            return ans
        
        ans = 1 + self.dfs(root.left, root.val) + self.dfs(root.right, root.val)

        return ans
