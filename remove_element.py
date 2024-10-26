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

class Solution1:
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

Plan.
iterate through array with left pointer.
place right pointer at end
while left < n:
    if left is val:
        if right is not val:
            swap
        HOLD ON!
Kinda like move zeroes...
ACTUALLY EXACTLY LIKE MOVE ZEROES
do things differently this time.
right pointer will be at end
it will move back if it is equal to val


Implement:
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums)-1

        while right > left:
            if nums[left] == val and nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            left += nums[left] != val
            right -= nums[right] == val
        while nums and nums[-1] == val:
            nums.pop()
        return len(nums)
"""
Review.
This makes me think, "What was I thinking when I wrote that complicated code for 'remove zeroes'
But actually, this one reorders nums, so there's a difference.

Evaluate:
Space: O(1)
Time: O(n)
"""