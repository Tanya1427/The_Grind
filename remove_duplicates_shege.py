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
duplicate_value = 1
counter = 0

while True:
    while current.next

"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        temp = ListNode("HI")
        temp.next = head

        previous = temp
        current = previous.next
        duplicate_value = current.val
        counter = 1

        while current:
            # print(counter, duplicate_value, current.next.val)
            if current.next and current.next.val == duplicate_value:
                counter += 1
                current = current.next
                # continue
            if counter > 1:
                previous.next = current.next
            print("Counter: ", counter, duplicate_value)
            previous = current
            current = current.next
            if current:
                duplicate_value = current.val
            counter = 1

        return temp.next
