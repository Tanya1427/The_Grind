"""
Understand.
One pass is possible.
nth from end is sz - n from start
Might be the first node that needs to be removed
n <= sz. n >= 1!

Match.
Fast|Slow pointer

Plan.
set a temp_head to empty node, length = pos = 0
fast, slow = head, temp_head
move both fast and slow until fast is spent:
    length += 2, pos += 1 while doing this.

If slow has gone over length - n, change it to temp_head (where it started)
if not, just continue till you reach before length - n
then remove node at length - n using slow.next = slow.next.next

return temp_head.next

Implement.
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp_head = slow = ListNode()
        temp_head.next = fast = head
        pos = length = 0

        # Get `length` `fast` while already moving `slow` through
        while fast and fast.next:
            length += 2
            pos += 1
            fast = fast.next.next
            slow = slow.next

        length += bool(fast)  # `Length` is odd if `fast` is not None
        remove = length - n

        # Reset `slow` if it's gone over `remove`
        if pos > remove:
            slow = temp_head
            pos = 0

        # Move `slow` toward `remove`
        while pos < remove:
            slow = slow.next
            pos += 1

        # Remove node at `remove`
        slow.next = slow.next.next

        # Return the head
        return temp_head.next

"""
Review.
If node is 1, slow will be temp_head.
temp_head.next = temp_head.next.next is used for removing head.
note resetting of slow to temp_head, not head.

!!!IMPORTANT!!!
Better plan seen from solution.
move a pointer to node `n` first,
create a new pointer, thne move until the first pointer is null.
the second pointer's next will be the node for removal.
ELEGANT! in my opinion.

Evaluate.
Space: O(1)
Time: O(n) (worst O(n+n/2))
"""
