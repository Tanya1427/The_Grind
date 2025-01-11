"""1400 Construct K Palindrome Strings.
Topics: Hash Table | String | Greedy | Counting

Understand.
ALL the characters.
Palindrome can have odd/even length...
annabelle, k=1

elanbnale, for 1 palindrome, there must be 2 of almost every character 
A palindrome is even number of a group of characters. having one character with odd count
if k==n, return true... k > n, return false
E.g aaaaii
annabelle => aabeellnn.
a: 2, b: 1, e: 2, l:2, n: 2
k palindromes can be constructed if counts can come together

What if count is greater than 2, maybe just take say, a: 4 as a: 2, a:2 - might help.
Question is asking if you can group letters well to make k.

2, 1, 2, 2, 2
4 evens 1 odd, k = 2. Yes.

Mississippi
M: 1, i: 4, s: 4, p: 2
1, 4, 4, 2. 3 evens 1 odd. , k=1, 2,3,4,5,6,7,8

1, 2, 1, 3: k=3

If only 1 is odd, k=1 is possible.

Match:
Greedy. Counting. Palindrome

Plan.
Count all. Use a [0] * 26 array to count.
COunt how many have odd counts, separate the even out of them
    i.e make them have count of 1. 5 => 4+1
    Get the sum of those ones => sum_ones
Get the sum of even counts: That's one palindrome.

sum_ones is the min number of palindromes str can have.
sum_twos can supplement.

say sum_ones = 5 (5 odd counts)
sum_twos = 12     (Whatever amount)

k = 4 can't work, k = 5? Yes!
 1   1   1   1   1 => odds, the evens can wrap around conviniently.
 
k = 6, yes! Remove 2 evens, the rest can wrap around well.
Could this be it? For every "excessive" in k, remove 2?

k=7, yes! Add two "odds" from sum_twos so that there are 7 odds.
if k < sum_ones, if k > total: false k==total? True

k=8? Yes. Add two "odds"(ones) and one even(two) to the odds.
1  1  1  1  1, 2  1  1, odds now 8, the rest of sum_twos can wrap around

x = k - sum_ones
If x is odd:
    You HAVE to remove even number y from sum_twos
     that you can share into x places.
    a greedy option is x+1 (x-1 can't be shared into x places :) )
    That'd make: 2. 1 1 1 1... that sum to x+1
    if you can remove x+1 from sum_evens, you're good (return true)
    Notice that sum_twos-(x+1) is even.
    return sum_twos >= x+1

if even:
    remove see if x/2 can be removed from sum_twos,
    This will share the x/2 into odds

Implement
"""

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        sum_ones, sum_twos, n, ORD_A = 0, 0, len(s), ord('a')
        ch_count = [0] * 26
        for ch in s:
            ch_count[ord(ch) - ORD_A] += 1

        for count in ch_count:
            is_odd = count & 1
            sum_ones += is_odd
            sum_twos += count - is_odd

        if k < sum_ones or k > len(s):
            return False

        x = k - sum_ones
        return sum_twos >= x + 1 if x & 1 else sum_twos >= x // 2


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return len(s) >= k >= sum(count & 1 for count in Counter(s).values())

"""
Reviewed above.

Evaluate:
Space: O(26) in counter => O(1)
Time: O(n) to make counter, n = len(s)

Thoughts:
This was a VERY GOOD question.
"""