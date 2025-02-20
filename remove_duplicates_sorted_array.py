"""
Understand.
Modify nums to have uniques in front
You don't need to pop(i)
3 * 10**4 means some O(n**2) would work - do better

Match.
Two pointers.

Plan.
set i and j to 0 and 1
if move far with j till nums[i] != nums[j]
set nums[i + 1] which is next of i to nums[j]
could be done with one loop

Implement.
"""

class Solution:
    def removeDuplicates(self, nums):
        i, j, n = 0, 0, len(nums)
        while i < n and j < n:
            if nums[i] == nums[j]:
                j += 1
                continue
            i += 1
            nums[i] = nums[j]
        return i + 1

"""
Reviewed.

Evaluate:
Space: O(1)
Time: O(n)
"""
