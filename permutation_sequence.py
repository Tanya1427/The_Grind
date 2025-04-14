"""
Understand.
(I got an inspiration for how to get the kth permutation yesterday.
I think it's brilliant!)
Understand: You don't need to get all possible permutations.

Match.
Combinatorics?

Plan.
To check if a permutation can start with a character,
 one can get how many possible permutations can be made
 with the remaining characters
E.g. abcd
if a is picked, bcd can be arranged in 6 ways,
 so a will be the first character in the first 6 permutations

Using this knowledge. Iteratively loop until all digits are spent,
 choosing the first, second, third, etc. digits accordingly.
 do by checking if current character is in it's right position and
  Subtracting the factorial of the remaining digits from k

Use a Python Dict to keep track of characters.
deleting is fast, and it maintains sorted order
   (This is not very necessary because the max count is 9,
   and deletion is not that bad)

Implement.
"""

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digits = dict.fromkeys(range(1, n + 1))
        kth = 0
        perm = math.factorial(n - 1)
        while n:
            for d in digits:
                if perm >= k:
                    break
                k -= perm
            del digits[d]
            kth = kth * 10 + d
            n -= 1
            perm //= n or 1
        return str(kth)

"""
Review:
Note that re-computing permutations is time consuming.
Did test case 5, 120 to check. worked.
Figured that stringbuilder not needed.
    Iteratively building integer is better

Evaluate:
Space: O(1) only saving max 9 stuff that would be removed
Time: O(n**2) -> To make `digits`, compute the permutation, and str(kth) O(n)
                 to loop while >> for loop O(n**2), so choose O(n**2)
But n max is 9, so O(9**2) => O(81) =...=> O(1).
Time: O(1)
"""
