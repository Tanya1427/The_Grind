"""
Understand.
Follow-up says to do without extra space.
BST is a type of sort.

Match.
Binary Tree. BST. In-order Traversal.

Plan.
Imagine you have a sorted array, how would you get the mode...
- you can count the elements since they are close to each other.
If you don't want to keep the count of each element...
First get the maximum frequency in the array,
in the next traversal, if an element's count is that max frequency, 
it is a mode.
Apply the same to the BST. by doing an In-order Traversal,
 you'd be able to move through the tree values as though it was a sorted array.
To know the element that was before, set it to some placeholder first, 
 then save it whenever you process a node.

Implement.
"""

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # First get the maximum frequency.
        freqs, prev = [1, 1], ['N']
        def count(tree):
            tree.left and count(tree.left)
            freqs[0] = 1 + freqs[0] if tree.val == prev[0] else 1
            freqs[1], prev[0] = max(freqs), tree.val
            tree.right and count(tree.right)
        count(root)

        prev[0], freqs[0], modes = 'N', 1, []
        def mode(tree):
            tree.left and mode(tree.left)
            freqs[0] = 1 + freqs[0] if tree.val == prev[0] else 1
            freqs[0] == freqs[1] and modes.append(tree.val)
            prev[0] = tree.val
            tree.right and mode(tree.right)
        mode(root)

        return modes

"""
Review.
max freq is largest element, middle element, smallest.

Evaluate.
Space: O(1). freqs, prev (call stack does not count)
Time: O(n). n -> for getting the highest freqency only 
         || n -> for saving those that have that frequency
"""