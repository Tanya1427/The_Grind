"""
Understand:
Word length doubles after every operation.
it will take math.log2(k) operations to get wordlen to k
a
ab
abbc
abbcbccd
abbcbccdbccdcdde
abbcbccdbccdcddebccdcddecddedeef

word started as 'a', so every xth char is 'b'
x: (start from 0)
1, 2, 4, 8, 16
x -> 2**n, n =0,1,... for 'b'
I.e. the 2**nth + 1 character is 'b'

'a' will only come after 'z'

For 'c'
3, 5, 6, 9, 10, 12, 17, 18, 20, 24
For 'c': 2**n+2**0, 2**n+2**1, ..., 2**n+2**n-1...
For 'c' subtract largest power of 2, answer is power of 2.
n=1

For 'd'
7, 11, 13, 14, 19, 21, 22, 25, 26, 28

2**2 + 3, 2**3 + 3, 2**3 + 5, 2**3 + 6, 2**4 + 3

Essentially adding 'c' to 2**n...


For 'e'
15, 23, 27, 29, 30
2**3 + 7, 2**4 + 7, 2**4 + 11 -> adding 2**n... to 'd'


Match:
Math.

Plan.
Brute force: Generate the string, any way possible, get [k-1]

Math...
Choose which character will undergoe math.log2(k) number of transformations...
  and 'add' to it... Might not work

... after about 30 minutes of Understanding...
Plan.
get how many times a 2**x needs to be subtracted to reach a 2**y or 0
Essentially, convert the number to base 2 :cries:
For 'b', you need to remove 2**x only once.
For 'c', twice, for 'd' thrice. 27 -> 2**4 + 2**3 + 2**1 + 2**0
                                23 -> 2**4 + 2**2 + 2**1 + 2**0

Answer == ascii_lowercase[(bin(x-1).count('1')) mod 26]

Say I don't want to use bin()
Python to the rescue: ascii_lowercase[(k-1).bit_count() mod 26]
How is .bit_count implemented internally?

bitcount(n) -> 1+bitcount(n-(2**x <= n))
bitcount(13) == 1+bitcount(13-8)=1+1+bitcount(5-4)=1+1+1

"""

class Solution:
    def kthCharacter(self, k: int) -> str:
        return ascii_lowercase[(k-1).bit_count() % 26]

"""
Reviewed

Evaluate:
Time: O(log2(K)) -> time to convert to binary.
Space: O(1). Cooler way would have been `return chr(... % 26 + ord('a'))`
"""
