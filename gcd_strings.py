"""
Understand.
s|t if s = t+t+t+t+t ... +t
addaddaddadd
addadd

addadd

=> addadd

a
a
=> a

gcd must be a substring of both.
MUST.

There could be a hint on odd and even length

Both should have same set of characters
Discussion seems to say it's a math problem :)
What is gcd, exactly?

12 8
12 = 8*1 + 4
4 = 1*4 + 0

GCD == 4

ababab  abab
ababab = abab*1 + ab
abab = ab*2 + 0
answer = ab

From similar question... 1979
while small:
    big, small = small, big % small
return big

ABCDE
ABC

ABCDE = ABC*1 + DE
ABC 

Go in reverse?

Match
Plan
BRUTE.
Move with two pointers.
i, j
if [i] == [j]:
    try with [:i+1]
Nah! One pointer is fine!
def is_divisor(string, div):
    # Split, if divisor, array will have "" all through.
    return bool("".join(string.split(div)))

Implement
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def is_divisor(string, div):
            n = len(string)
            d = len(div)
            if n % d == 0:
                return div*(n//d) == string
            return False
        i = end = 0
        for i in range(min(len(str1), len(str2))):
            if str1[i] != str2[i]:
                return ""
            if is_divisor(str1, str1[0:i+1]) and is_divisor(str1, str1[0:i+1]):
                end = i
        return str1[:end+1]*(end != 0)

"""
Plan:
Had to check a solution to code this.
Should be same if they have a common divisor.
1apple + 3apples = 3apples + 1apple = 4apples :)

Now imagine if it WERE apples.
The GCD of two apple collections will be the GCD of their lengths, right?
[AP] == apple
[AP][AP][AP][AP][AP][AP][AP][AP][AP][AP][AP][AP] and [AP][AP][AP][AP][AP][AP][AP][AP]
is just 12 and 8. Their GCD is 4, for set of apples should divide both piles.

IMPLEMENT
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""

        lens = [len(str1), len(str2)]
        big, small = max(lens), min(lens)
        while small:
            big, small = small, big % small
        return str1[:big]

"""
Reviewed:
Evaluate:
Time: O(m|n)? where m and n are len str1 and str2. gcd is logarithmic.
Space: 
"""
