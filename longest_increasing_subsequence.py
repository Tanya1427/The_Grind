"""
Understand.
strictly increasing Subsequence
input: nums
return answer <= len(nums)
nums[i] can be negative. nums.length max => 2500 (brute force n**2 should work)


... what is the min, what is the max. WHERE is the min, where is the max.
Match.
Array.

Plan.
Plan: Start with brute force, see if you can optimize. Take note of stuff.
*NOTE* if you start with a big number, you'll go nowhere.
    How about a prefix min/max...
Brute force.
Recursion.
Multiple branching. O(n**n) :(

Tips. "Set" things. if there are two 5's, you should
only branch out for 1 of them.
Do not branch for the rest
consider [3, 2, 1, 5,  6, 5, 10]

set max_length, length= 0

def find_length(index, length):
    max_length = length
    for next_index in range(index+1, n):
        next_num = nums[next_index]
        if next_num > nums[index] and next_num not in track:
            max_length = max(max_length, find_length(next_index, length+1))
    return max_length

Sub-obtimal. No repeat. No greater branch.
def find_length(index, length, track):
    for next_index in range(index+1, n):
        next_num = nums[next_index]
        if next_num > nums[index] and next_num not in track:
            track.add(next_num)
            find_length(next_num, length+1, track)
            track.remove(next_num)

max_length = max(max_length, length)

DP.
Use a dictionary to keep track of visited indices.
Somehow, the don't do greater thing didn't work...
return max_length

Implement:
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length_cache = {}
        def find_length(index):
            if index in length_cache:
                return length_cache[index]

            max_length = 1
            for next_index in range(index + 1, n):
                if nums[next_index] > nums[index]:
                    max_length = max(max_length, 1 + find_length(next_index))

            length_cache[index] = max_length
            return length_cache[index]

        return max(map(find_length, range(n)))
"""
Reviewd

Evaluate:
Space: O(n)
TIme: O(n**2)

"""
