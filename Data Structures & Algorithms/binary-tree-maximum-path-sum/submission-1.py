# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')

        def dfs(root):
            nonlocal res            
            if root is None:
                return 0
            left_sum = dfs(root.left)
            right_sum = dfs(root.right)
            left_sum_with_node = root.val + left_sum 
            right_sum_with_node = root.val + right_sum
            sum_of_nodes = root.val + left_sum + right_sum
            res = max(sum_of_nodes, left_sum_with_node,
                   right_sum_with_node, root.val, res)
            return max(left_sum_with_node, right_sum_with_node, root.val)

        left_sum = dfs(root.left)
        right_sum = dfs(root.right)
        res = max(left_sum + right_sum + root.val, left_sum + root.val,
        right_sum + root.val, root.val, res)

        return res
