# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Understand.
No duplicates.
[0, 1, 2, 3, 4, 5, 6, 7]
binary tree.

Match:
BST. Alright, Recursion.

Plan.
left -> [0, 1, 2, 3]
mid = 4
right -> [5, 6, 7]

node = TreeNode(4)
node.left = makeTree(left)
node.right = makeTree(right)

return node


Implement:
"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def make_tree(start, end):  # prevent passing in slices - memory
            if start == end:
                return None
            mid = (end+start) // 2
            sub_tree = TreeNode(nums[mid])
            sub_tree.left = make_tree(start, mid)
            sub_tree.right = make_tree(mid+1, end)
            return sub_tree

        return make_tree(0, len(nums))

"""
Review:

[0, 1, 2, 3, 4, 5, 6, 7]
start = 0
end = 8
mid = 8//2 = 4

    left
    start = 0
    end = 4
    mid = 4//2 = 2

                    4


Evaluate:
O(n) time. O(n), recursion depth, space (All nodes will be "called for")
"""


"""
Understand.
[1, 2, 3, 4, 5, 6, 7]

                        5
                2               6
            1       3       5       7

Match:
BST. BFS. Iterative solution

Plan.

"""

class SolutionIter:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        mid = n // 2
        add = round(n / 4)
        root = TreeNode(nums[mid])
        tree_nodes = {mid: root}  # could make this an array
        positions = (("left", -1), ("right", 1))
        queue = deque([mid])
        while queue:
            length = len(queue)
            for _ in range(length):
                mid = queue.popleft()
                parent_node = tree_nodes[mid]
                print(mid)

                for child, dif in positions:
                    node_index = mid + dif*add
                    if node_index in tree_nodes or node_index >= n:
                        continue
                    child_node = TreeNode(nums[node_index])
                    tree_nodes[node_index] = child_node
                    setattr(parent_node, child, child_node)
                    queue.append(node_index)
            add = round(add/2)
        return root
