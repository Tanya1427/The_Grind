"""
UMPIRE
Understand:
Case all==1, return n-1
case all==0, return 0
n=1 0 0

Match:
Array, Dynamic Programming, Sliding Winodw, Two Pointers

Plan/Pseudocode:
Maintain a sliding window where there is at most one zero in it.

[1,0,1,1,1,0,1,1,0,1]

sliding window, slider
longest = 5

slider [1, 1, 1]
count0 = 1

at position 5, delete every until position 1
reset count0 from 2 to 1
continue
longest = 0

count0 = 1|2
longest = max(longest, count1)
count1 = count1 - count_before
count_before = count1
count = 1
.............................................

Implement:
[1,1,0,1]
"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        try:
            start = nums.index(0)
        except:
            return n-1
        count_before = start
        count1 = count_before
        longest = 0
        count0 = 0

        for i in range(start+1, n):
            count1 += nums[i]
            count0 += 1-nums[i]

            if count0 == 1:
                longest = max(longest, count1)
                count1 -= count_before
                count_before = count1
                count0 = 0
        
        if nums[-1] == 1:
            longest = max(longest, count1)

        return longest

"""
Review
nums =
[0,1,1,1,0,1,1,0,1]
Output
3
Expected
5

Evaluate:
Space: O(1)
Time-Space: O(n)

"""

