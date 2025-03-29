"""
Understand.
O(n**2) won't work. n max is 10**5.
Modular arithmetic == "multiple of k"
len(subarray) > 1

Match.
Prefix sum. Mod.

Plan.
Interesting plan.
Make cummulative sums out of nums (zero is the first sum)
    # You can get every possible sum from a cummulative sum array,
    # using the difference between two...
To minimize this sum, do sum_i % k for each cummulative sum
    # If the difference between any two cummulative sums is zero, 
    #     then the sum between that portion of the entire array
    #         is divisible by k (we're summing reminders)

So we need to check for duplicates of % k of cummulative sums,
 and make sure subarray len > 2
To make sure subarray len > 2,
 save the index of first cummulative sum % k
 , then check diff of duplicate. If diff > 1, good.

Implement.
"""

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sum_i, duplicate = 0, {0: -1}
        for i, x in enumerate(nums):
            sum_i = (sum_i + x) % k
            if sum_i in duplicate:
                if i - duplicate[sum_i] == 1:
                    continue
                return True
            duplicate[sum_i] = i
        return False

"""
Reviewed.
Thoroughly.
First code failed
[5,0,0,0]
3 --> returned False
Because it updated index immediately, index diff was always == 1
index should be updated after diff > 1

Evaluate:
Space: O(n) -> for hash map.
Time: O(n) -> one pass for loop.
"""
