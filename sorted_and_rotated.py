"""
Understand.
[i] <= [i+1] for all in sorted.

Match.
One-liner.

Plan.
Count how many instances where the next number
 is less than the previous. Wrap around and count.
return count <= 1. or < 2.
Would have been == 1, but consider nums[i] == x for all i.
If there is more than 1 anomaly, it couldn't have been (sort+rotat)ed

Implement.
"""
class Solution:
    def check(self, nums: List[int]) -> bool:
        return sum(nums[i] < nums[i - 1] for i in range(len(nums))) < 2

"""
Review.
[2,1,3,4] made me realize wrapping.

Evaluate:
Space: O(1)
Time: O(n)
"""
