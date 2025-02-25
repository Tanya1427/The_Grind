"""
Understood.

Match.
Math. Prefix sum.

Plan.
Get cummulative sum array.
from one point get number of opposite parity sums to end
    (using another prefix_sum to compute the number of odds/evens)
sum these numbers

arr=>[ 7,  4,  1,  5,  5,  8, 4]
sums=>[34, 27, 23, 22, 17, 12, 4, 0]
odds=>[ 3,  3,  2,  1,  1,  0, 0, 0] -> odd prefix
evens=>[ 5,  4,  4,  4,  3,  3, 2, 1] -> even prefix

Do without space, compute number of even/odd sums backwards.

Implement.
(first did arr.append(0) then n - 1 to -1 step -1.
Removed append and adjusted indexes and starting values)
"""
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        sums = arr[-1]
        odds = add = sums & 1
        evens = 1 - add
        odd_sums = 0
        for i in range(n - 1, -2, -1):
            odd_sums += evens if add else odds
            sums += arr[i]
            add = sums & 1
            odds += add
            evens += 1 - add
        return odd_sums % (10**9 + 7)

"""
Reviewed.
Added modulo 10**9 + 7

Evaluate.
Space: O(1)
Time: O(n)
"""