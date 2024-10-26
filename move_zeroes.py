"""
Understand: shifiting?
How to shift
[0, 0, 1, 1] => [1, 1, 0, 0]

Match
Two pointers

Plan
Informed swapping?
[0, 1, 0, 3, 12] => [1, 3, 12, 0, 0]

zero_pointer will get first zero, next one will move until it sees none zero,
when it does, they'll swap, the one that has gone ahead will come back to the zero_pointer.

[0, 1, 0, 3, 12]

z   n
[1, 0, 0, 3, 12]

    z     n
[1, 3, 0, 0, 12]
       z      n
[1, 3, 12, 0, 0]
DONE
set find_zero, find_num to 0
while find_num < n or find_zero < n:
    if nums[find_zero]:  # NOT 0
        find_zero += 1
        continue
    if nums[find_num]:
        if not nums[find_zero]
            swap find_num and zero
            find_num += 1
            find_zero += 1
        continue
    find_num += 1

"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 not in nums:
            return
        find_zero = nums.index(0)
        n, find_num = len(nums), find_zero+1
        while find_num < n and find_zero < n:
            if nums[find_zero]:  # NOT 0
                find_zero += 1
                continue  # No need to find_num when there's no zero yet?

            if nums[find_num]:
                if not nums[find_zero]:
                    if find_num > find_zero:
                        nums[find_zero], nums[find_num] = nums[find_num], nums[find_zero]
                        find_zero += 1
                    find_num += 1
                continue  # Continue, try to find_zero
            find_num += 1
"""
Reviewed

Evaluate
Space: O(1)
Time => O(n)
"""