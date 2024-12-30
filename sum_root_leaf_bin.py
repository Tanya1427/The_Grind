# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Understand:
1010101 => 100+101+110+111 = 4+5+6+7=22
2**n

Match:
DFS. Cummulative sum. Math.

Plan:
Try to use minimal memory.
 (Of course there's already the call stack to worry about)

Way to do that: Compile the sum. next sum = 2*previous sum + current val
return left_sum + right_sum
Total is sum of left and rights - from leaves.
Leaves have no total.

Implement:
"""
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def get_sum(tree, current_val):
            current_val = current_val*2 + tree.val
            total = 0
            if tree.left:
                total += get_sum(tree.left, current_val)
            if tree.right:
                total += get_sum(tree.right, current_val)

            if not (tree.left or tree.right):
                return current_val
            return total

        return get_sum(root, 0)

"""
Review:
T => Tree
get_sum(T(1), cur_val:=0)
    cur_val = 0*2 + 1 => 1
    total = 0
		
    left: get_sum(T(0), cur_val:=1)
        cur_val = 2*1 + 0 => 2
        total = 0
		
        left: get_sum(T(0), cur_val:=2):
            cur_val = 2*2 + 0 => 4
            total = 0
            return cur_val ==> 4

        total = 0 + 4 => 4

        right: get_sum(T(1), cur_val:=2):
            cur_val = 2*2 + 1 => 5
            total = 0
            return cur_val ==> 5

        total = 4 + 5 => 9
        return total ==> 9

    total = 0 + 9 => 9

    right: get_sum(T(1), cur_val:=1)
        cur_val = 2*1 + 1 => 3
        total = 0

        left: get_sum(T(0), cur_val:=3):
            cur_val = 2*3 + 0 => 6
            total = 0
            return cur_val ==> 6

        total = 0 + 6 => 6

        right: get_sum(T(1), cur_val:=3):
            cur_val = 2*2 + 3 => 7
            total = 0
            return cur_val ==> 7

        total = 6 +7 => 13
        return total ==> 13

    total = 9 + 13 => 22
    return total ==> 22

Evaluate:
Time: O(n) n-> nodes
Space (not call stack): O(1)
"""
