# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Understand.
Reverse linkedlist S25 Ultra

Match.
Recursion.

Plan.
Make things easy.
Get length and move to the node that marks the remainder of the linked list
    after dividing into groups of k
save that node as `stop`

define function rev_group that reverses a linked list up to the kth node
and returns the head of the reversed.
    set the end of the reversed list,
        to the next recursion call having the next node as input
    the recursive function stops when input is `stop` variable.
    (`stop` could be None)
return the group-reversed linkedlist.
Traverse to get the end, and set that node's next to `stop`

return the group-reversed linkedlist

Implement.
"""

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n, node = 0, head
        while node:
            node = node.next
            n += 1
        i, node = n - n % k, head
        while i:
            node = node.next
            i -= 1
        stop = node

        def rev_group(head):
            if head is stop:
                return
            node = head
            temp_head = None
            first = node
            count = 0
            while count < k and node:
                hold = node.next
                node.next = temp_head
                temp_head = node
                node = hold
                count += 1
            first.next = rev_group(node)
            return temp_head
        body = rev_group(head)
        node = body
        while node.next:
            node = node.next
        node.next = stop
        return body

"""
Review.
One variable, k = 1.
Maybe recursive function could also return the last node.

Evaluate:
Space: O(k) due to call stack, O(1) not considering call stack.
Time: O(n) - n is length of linked list.
"""
