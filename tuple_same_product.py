"""
Understand.
DISTINCT - helpful.
NUMBER of tuples. not the tuples themselves.
nums[i] is positve and non-zero. len = 1000. O(n**3) might work.
a, b, c, d can form many. abcd is a perfect square.
ab == cd == abcd ** 0.5
nums[i] max is 10000. **4 => 10000000000000000, can't check all squares
... Odds evens in making squares...

Match.
Math.

Plan.
Don't check hints/topics.
Save indices.
do a triple, distinct loop:
    calculate 4th
    if it's perfect square...
    get all 4. permute them...

B.
get all products of pairs, xy. DISTINCT.
Rest assured that they'll be no same products repeated.
n_abcd = 0
count the products.
for each product count:
    n is number of appearance.
    match n.
    2: there is an a, b, c, d, that ab is cd. there are 8 ways of arranging this.
    3: say x1y1, x2y2, x3y3 can pair with themselves 3 distinct ways to make ab==cd
        3*8 => 24
    4: x1y1, x2y2, x3y3, x4y4, pairs 6 times...
    n: x1y1, x2y2, ..., xnyn, pairs (n-1) + (n-2) +...+1 times
        I.E. n(n-1)/2. multiplied by 8
    add 4n(n-1) to n_abcd.
return n_abcd

Implement.
"""
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        return sum(4*x*(x - 1) for x in Counter(nums[i] * nums[j] for i in range(len(nums)) for j in range(i + 1, len(nums))).values())

"""
Reviewed.

Evaluate:
Space: O(n**2) for saving count of products
Time: O(n**2) for getting count of products. O(n**2) for summing counts
"""