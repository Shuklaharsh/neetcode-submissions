# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        q = deque()
        q.append(root)
        res = []

        while q:
            curr_size = len(q)
            while curr_size:
                curr_node = q.popleft()
                if curr_size == 1:
                    res.append(curr_node.val)
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)

                curr_size -= 1

        return res

