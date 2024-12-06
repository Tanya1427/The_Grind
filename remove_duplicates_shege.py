# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Understand.
Remove duplicates from sorted lists on steroids

Match.
Temp Head. LinkedList

Plan.
set temp to ListNode("HI")
set temp.next to head
current = temp
fast
current.val = 1
counter = 0

while True:
    while current.next

"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head

        temp = ListNode("")
        temp.next = head
        previous = temp
        current = previous
        behind = current  # Don't want to many .nexts

        while current:
            if current.next and current.val == current.next.val:
                behind = current
                current = current.next
                continue

            if behind.val == current.val:
                previous.next = current.next
            else:
                previous = current
            current = current.next

        return temp.next
