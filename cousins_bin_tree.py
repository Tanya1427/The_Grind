# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Understood.
Match:
BT, BFS-Level-order
Plan:
Level order traversal with a twist - save the values into set
Implement:
"""

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque([root])
        x_y = {x, y}
        while queue:
            found = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                found += node.val in x_y
                if found == 2:
                    return True
                if node.left and node.right and {node.left.val, node.right.val} == x_y:
                    return False

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return False
"""
Reviewed
Evaluate:
n -> number of nodes
Space: O(n)
Time: O(n)
"""