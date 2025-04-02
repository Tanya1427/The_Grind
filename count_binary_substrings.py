"""
Didn't want to UMPIRE but this question is really good.
Understand.
s[i] is '0' or '1'
s.len is 10**5, O(n**2) will fail.

Match.
Counting.

Plan.
Run through this
00 11 00 11
2  2  2  2

0011 01 1100 10 0011 01 

Notice that adjacent counts are the ones that produce these binary substrings
if there are x [0s | 1s] and y [1s | os] in an adjacent count.,
    then the number of binary substrings they produces
    turns out to be min(x, y) - cool!
Algorithm:
set prev_char to "0"; prev_count to 0; current count to 0; otal to 0
start looping through string with char:
    if char is prev_char: add to current_count
    else: add min of both counts to total;
        change prev_count to current_count;
        change current_count to 1

Implement.
"""

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev_count = cur_count = total = 0
        char = s[0]
        for ch in s:
            if ch == char:
                cur_count += 1
                continue
            total += min(prev_count, cur_count)
            prev_count, cur_count = cur_count, 1
            char = ch
        return total + min(prev_count, cur_count)

"""
Review.
000 11 00 11 0 1
3   2  2  2  1 1
cur = 0
prev = 2
total = 4
(forgot to add char = ch)
  |
00110011
cur = 2
prev = 0
total = 0

Evaluate:
Space: O(1)
Time: O(n)
"""
