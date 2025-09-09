# I'm back!
"""
UMPIRE
Understand.
Input: s: str, k: int
Choose any character, replace it with any other character., k times.
Return len longest substring.
A string can be made to be uniform in k steps if the total count of characters except the most frequent is <= k

Match.
Dynamic Sliding Window
Counting

Plan.
For each substring, get highest frequency of a character, get number of other characters.
- check if it's <= k. Update max length of substring as required.

set max_length = 1
Use a left and right pointer to start at 0th character.
If condition is fulfilled (i.e. n_other_chars <= k), expand window.
Else. Slide window. (Don't shrink since we are looking for max_length)
Use count<chr, map> to keep track of character count,
Update character count, and the highest_frequency as you slide and expand through window.
do until r == n

Implement.
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 1
        left, right = 0, 0
        count = defaultdict(int, {s[0]: 1})
        highest_freq = 1
        while right < n - 1:
            right += 1
            count[s[right]] += 1
            highest_freq = max(highest_freq, count[s[right]])
            len_sub = right - left + 1
            if len_sub - highest_freq <= k:
                max_len = max(max_len, len_sub)
            else:
                highest_freq -= highest_freq == count[s[left]]
                count[s[left]] -= 1
                left += 1

        return max_len

"""
Review.
 D N I N N A D F N N
 | |
1
maxx = 1
count = {D: 1}
highFreq = 1
Works...

Evaluate.
Space: O(1). Counter will take max 26 keys.
Time: O(n), right pointer is always moving.
"""

