"""
Thanks to discussion for the hint on prime squares.
Plan:
Get the squareroot of the number.
If it is an integer (%1), check if it's prime.
To check if it's prime, loop to it's squareroot.
increment loop by 6.
Check 6k+1 and 6k-1 if num is divisible by them.

Evaluate:
Space: O(1)
Time: n -> sqrt(n) -> sqrt(sqrt(n)) -> sqrt(sqrt(n))/6
10**4 -> 10**2 -> 10 -> 1.6666
Essentially O(1)
"""
class Solution:
    def isThree(self, n: int) -> bool:
        # base case
        if n == 1:
            return False

        sqrt_n = n**0.5
        if sqrt_n % 1:
            return False

        sqrt_n = int(sqrt_n)

        # 2 and 3 are prime
        if sqrt_n in {2, 3}:
            return True

        # Check if divisible by 2 or 3 (6k+1 won't work for these two)
        if not (sqrt_n % 2 and sqrt_n % 3):
            return False

        divisor = 6
        sqrt_sqrt_n = int(sqrt_n**0.5)

        while divisor < sqrt_sqrt_n:
            # Get reminder for 6k +/- 1
            if not (sqrt_n % (divisor+1) and sqrt_n % (divisor-1)):
                return False
            divisor += 6

        return True