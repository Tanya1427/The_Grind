"""
Understand.
2 and 5 - and 10?
n = 10^4, O(n) should work.

Match.
Mat h.

Plan.
Count the number of multiples of 5.
no need to count number of multiples of 2 because
  there will always be a multiple of 2 to make 5 reduce to ...0
In number of multiples of 5, get 5**2, 3, 4, up to where it stops in before n
5 will produce one 0; 25, 2; 125, 3; 625, 4; 3125, 5. (n <= 10^4)

Get the largest power of 5 before n.
large_5 = largest power of 5
5^exp = larg_5, save exp.
multiples_5 = 0

while large_5 != 1:
     multiples_large_5 = multiples_5 by exp * no of multiples of large
     subtract previous sums of large 5 multiples from multiples_large_5
     add multiples_large_5 to multiples_5
     exp -= 1
     large_5 //= 5

subtract to avoid repetition of multiples

Better, clearer plan
start from 5. add all multiples of 5
increase to 25. add all multiples of 25
don't worry about multiples of 10.
they are lowkey multiples of 5 powers and generate zeroes too.

thinking more.
that brings a geometric progression with common ratio 1/5
formula a/(1-r) for GP will give progression sum to infinity.
But to reduce the error, get max power of 5 just after n
get number of multiples of that power. (it'll be a float)
Get the sum of another GP with the prev computation as the first element
Get the limiting um to infinity.
subtract that from the previous. 

won't work. THere are floating parts in each term of the GP.
I can't approximate enough to reduce the floats.

log_5(n) working plan.
keep summing after division by 5 in a while loop

Implement.
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroes = 0
        while n:
            n //= 5
            zeroes += n
        return zeroes

"""
Reviewed.
All plans but the first one.
Settled for this.

Evaluate.
Space: O(1)
Time: O(log_5(n)). O(log n)
"""
