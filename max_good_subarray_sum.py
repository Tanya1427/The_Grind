"""
Understand:
Not unique, O(n**2) won't work, k is large.

Match.
Hashmap, prefix sum (cummulative sum), minmax

Plan.
get prefix-sum the array

make dictionary of 
nums[i] -> [prefix sum up to i]

but instead of having all prefix sum up to i, keep only the min prefix sum, and max prefix sum as you go.
i.e.
nums[i] -> [min_prefix_sum_of_nums[i], max_prefix_sum_of_nums[i]]


If you find a new max prefix sums of nums_i as max_i,
` nums[i] - nums[j] = k
` nums[i] - nums[j] = -k

check min_j = nums[i] - k and nums[i] + k if it's in the dictionary
    use max(curr_max, max_i - min_j) to update the max difference.

Implement
"""

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref = defaultdict(lambda: float("inf"))  # min prefix sum
        max_good_sum = float("-inf")
        summ = 0
        for i in range(n):
            x = nums[i]
            summ += nums[i]
            pref[x] = min(summ, pref[x])
            max_good_sum = max(max_good_sum, summ - pref[x - k] + x - k, summ - pref[x + k] + x + k)

        return max_good_sum if max_good_sum > float("-inf") else 0

"""
Review.
summ max_good_sum at -inf
check if x - k and x + k are in defaultdict before doing any updates becasue updates need x - k and x + k
    this does not need to be done x - k or x + k + -|+inf is still -|+inf
no need to build the prefix sum in nums, pref will take care of that.
You should use all prefix reached to check for max good subarray sum, not just the max prefixes - plan update
Which means no need to keep track of max prefix sum reached. Just update

Evaluate.
Space: O(n) worst case... - saving min for every element if distinct. (Best case is if all elements are the same)
Time: O(n) every case.

"""
