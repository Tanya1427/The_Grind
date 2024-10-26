"""
Understand:
Order doesn't matter

Match:
Sorting and Tricking

Plan :)
Make a lambda for list.sort that will make sorting push val to back.
count how many vals there are
pop() n_vals times.

NO NEED to count, just pop until...

Implementation:
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort(key=lambda x: float("inf") if x == val else x)
        while nums and nums[-1] == val:
            nums.pop()
        return len(nums)
"""
Reviewed.

Evaluate:
Space: O(1)
Time: O(nlogn)

"""