# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Understand:
Like rotate array???

Match:
Two pointers. Rotate array logic. Multiple passes. Maybe recursion. Maybe doublylinked


Plan.

Get length of list -> N
previous-linking them in the process
move second pointer to N-k
first pointer will always keep moving forward
move second pointer forward and back? Nah!

(I think doubly-linking it is extra space)
Understand
Linked list has head. The other part could be tail.

Match.
LinkedList. Two pointers. Multiple passes.

Plan:
get length of list -> N
save head
keep (N-k)th node.
Move to before (N-k)th node and set it's next to null
Move from (N-k)th node to end. (next=None)
set end.next to head

n=2, k=1
[1, 2]
new_head = [2]
head = [1]
new_head_end = [1]
"""

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # First pass to get the length
        n = 0
        linked = head
        while linked is not None:
            linked = linked.next
            n += 1

        if n < 2:
            return head

        k %= n  # Normalize k
        if k == 0:  # Fail-safe?
            return head

        # Another pass to get the (n-k)th (new_head) and the new end
        new_end = head
        i = 0
        while i < n-k-1:
            new_end = new_end.next
            i += 1
        new_head = new_end.next
        new_end.next = None  # Make it the new end.

        # Last pass to get the end of the new head
        new_head_end = new_head
        while new_head_end.next is not None:
            new_head_end = new_head_end.next
        new_head_end.next = head  # Make the former head the tail

        return new_head

"""
Reviewed
Evaluate:
Space: O(1)
Time: O(n)
"""
