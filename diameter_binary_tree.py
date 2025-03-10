"""
Understand.
May/maynot pass through root.
tree might not be balanced or complete
node values do not matter.

Match.
BT. DFS. Max height problem.

Plan.
@Kondwani Mwape
keep 'global' self.diameter var
Start at root.
self.diameter is height(left) + height(right)
recursively do so returning max.
before returning, update self.diameter var with max(diam, h(l)+h(r))
    return max(h(l), h(r)) in each call.
return diam

Implement.
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def height(tree):
            if not tree:
                return 0
            left = 1 + height(tree.left)
            right = 1 + height(tree.right)
            self.diameter = max(self.diameter, left + right - 2)
            return max(left, right)

        height(root)

        return self.diameter

"""
Reviewed.
Generated array of len==10**4-1 and tested.
Changed some of the values to null. Tested.

Evaluate.
Space: O(n) (call stack)
Time: O(n)
"""