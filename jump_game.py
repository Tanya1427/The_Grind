"""
Understand.
n**2 is impractical. nums[i] can be 0.
if nums[0] is 0, you're cooked.

Match.
DP. Greedy.

Plan.

DP. Try all possible jumps. Memoize.
2 can do once/twice. Not good. nums[i] > 100

[2,3,1,1,4]
save last index => 4.
starting from first index, loop to get best jump index.
best jump index is index i, for which diff := last-index - i - nums[i]
    is minimal.
If you reach index that last-index - i - nums[i] is 0, return True.
if you loop to reach last_index, return True.
else if lastindex-i-nums[i] <= diff: # Pick the one nearer to last index <=
    diff = lastindex-i-nums[i]
    best_index = i

Implement
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, last_index = 0, len(nums) - 1
        while i < last_index:
            best_index, index, best_diff = i, i, float("inf")
            stop_index = nums[index] + index
            if nums[index] == 0:
                return False

            while index < stop_index:
                index += 1
                diff = last_index - index - nums[index]
                if index == last_index or diff < 1:
                    return True

                if diff <= best_diff:
                    best_diff, best_index = diff, index
            i = best_index
        else:
            return True

"""
Reviewed.

Evaluate:
Space: O(1)
Time: O(n + m)? n = nums.length, m = max(nums)
"""