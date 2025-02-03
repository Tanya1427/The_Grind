"""
Understand.
Subarray not subsequence. n==50 brute force works.
STRICTLY increasing. - no duplicates check.

Match.
Counting.

Plan.
do for both increasing and decreasing with different variables
set max = 1
set count = 1
Move through the array from index 1
    if this index is greater than prev, increase count
    else:
        max = max of count and max
        count = 1

Implement
"""
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        nums.append(nums[-1])  # To ensure last number counts
        count_inc, count_dec, max_inc, max_dec = [1] * 4
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count_inc += 1
            else:
                max_inc = max(max_inc, count_inc)
                count_inc = 1

            if nums[i] < nums[i - 1]:
                count_dec += 1
            else:
                max_dec = max(max_dec, count_dec)
                count_dec = 1

        return max(max_inc, max_dec)

"""
Reviewed.
[1,1,5]

Evaluate.
Space: O(1)
Time: O(n:=len(nums))
"""
