"""
AUTHORED BY @Enochteo | @DanielOnGitHub17

Understand.
Length is 10**5 max. Won't hurt to do 10*length for slicing.
Number bases.

Match.
Rolling hash, hashmap switch. Math.

Plan.
Use base 4.
A=0, C=1, G=2, T=3
Get hash for first length-10 substring.

init hmap, result[]

Go through string starting from 0 -> when it will end.
Create new hash by:
    Remove starting character by removing first 'digit' in hash.
    Shift the resulting value to left in base 4 (<< 2)
    Add the end value
    if new hash found once before:
        don't do anything
    if never found:
        mark found
    if found once:
        slice repeating sequence and add to result

return result

Implement:
"""

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        digits = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        ans = []
        n = len(s)
        hv = 0
        MAX = 4 ** 9
        for i in range(10):
            hv = (hv << 2) + digits[s[i]]

        hmap = {hv: 0}

        for i in range(n - 10):
            hv = ((hv - MAX*digits[s[i]]) << 2) + digits[s[i + 10]]
            if hv not in hmap:
                hmap[hv] = 0
            elif hmap[hv] == 0:
                ans.append(s[i+1:i+11])
                hmap[hv] = 1

        return ans

"""
Reviewed:
+ comes before <<
slice from i+1-> i+11, not i-> i+10 cause of location of slice

Evaluate:
Space: O(n)
Time: O(n) substrlen is just 10
"""

# cheers!
