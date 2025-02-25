# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Understand:
Complete binary tree. 2**n nodes on each level n, n: 1, 2,...

Match:
Binary tree. Binary Search. Complete Binary Tree.

Plan:
start get the height as h. count from 0

Now, try to get number of nodes in end level.

Assume the tree is complete, the end node should have an index of n-1
if there are n nodes in the tree, and the tree is represented as an array.
n = 2**(h+1) (h is from 0), n is num nodes
end = n - 1
start = 2**h - 1, counting from 0
path = [0] * h

Binary search approach:
    mid = (start + end) // 2
    # Gener
    starting from head, go down to find the node that
     corresponds to that index.
    How? Well, use the complete property of left and right
    left: 2*i + 1, right: 2*i + 2
    starting from 0, you should be able to choose the next 
     (either left of right based on what mid is.
    supposing that works, go down n-1/so levels till you see None.
    If is None, you know to go left more: end = mid
    if you find something, you know to go right more: start = mid
    LOOP.

Pick the one that will make sure mid doesn't go above?
Or pick the one that will make mid even? Or odd. YES!!!.
The start left IS odd!, all lefts are odd because 2x + 1 is always odd.
similarly, all rights are even.
Makes me think, "BINARY!" 1/0. Odd/Even
Formula might be x-1/2 or x-2/2 in reverse?
Use log n space. Generate left/right 1/0 from bottom up, and then traverse backwards

"""

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        h, tree = 0, root
        while tree:
            tree = tree.left
            h += 1

        dirs = ("right", "left")
        n = 2**h - 1
        path = [0] * (h-1)
        end = n - 1
        start = 2**(h-1) - 1

        while end >= start:
            mid = (start + end) // 2

            # Make the path
            path_index = mid
            # Go in reverse the last operation to the first.
            for i in range(h - 2, -1, -1):
                path[i] = path_index & 1  # 0, right (even, 2 % 2). 1, left (odd).
                # (100 - 1) // 2 => 49, means that 100 came from 49*2 + 2.
                # 99 // 2 => 49. 99 Came from 49*2 + 1
                path_index = (path_index - 1) // 2

            # Now follow the path
            end_node = root
            for i in path:
                end_node = getattr(end_node, dirs[i])

            # Reached the end_node. Now check it.
            if end_node:  # Moved too left
                start = mid + 1
            else:  # Moved too right
                end = mid - 1

        return start  # Just after the last node!

"""
Reviewed.
Tested with n = 0 to 2000 in VS Code

Evaluate.
Space: O(log n)  # path[] has len(height)
Height -> O(log n)
while end >= start: log (n) 
    make_path -> log(n)
    follow_path -> log(n)
-> 2(log n)**2
Time: (log n)**2
"""