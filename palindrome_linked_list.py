# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Understand.
Follow up: O(n) time, O(1) space

Match.
Two pointers.

Plan.
Divide list into two equal lists.
    get the middle using fast and slow pointer method.
Reverse any of them
Check if they are equal (one node might be off)

Implement.
"""

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        # `slow` is middle after loop ends
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # skip replaceable middle if palindrome length is odd
        if fast is not None:
            slow = slow.next

        # Reverse the second head
        reversed_head, head2 = None, slow
        while head2:
            next_head = head2.next
            head2.next = reversed_head
            reversed_head = head2
            head2 = next_head

        # Go through both lists, to check if palindrome.
        # Stop at reversed_head which is shorter
        while reversed_head:
            if head.val != reversed_head.val:
                return False
            head = head.next
            reversed_head = reversed_head.next

        return True

"""
Review.
1. Misspelled reversed_head as revesed_head in reversal loop
2. Is there a way to use the fast/slow pointer loop
     to reverse the first head?

Evaluate.
Space: O(1) (whew)
Time: O(n) - three traversals!
"""
