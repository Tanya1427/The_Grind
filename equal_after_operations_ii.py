"""
Understand.
"34789"
7157 => (3 4) (4 7) (7 8) (8 9)
862 => (3 4 4 7) (4 7 7 8) (7 8 8 9)
48 => (3 4 4 7 4 7 7 8) (4 7 7 8 7 8 8 9)
3: 1, 4: 3, 7: 3, 8: 1
4: 1, 7: 3, 8: 3, 9: 1
11
121
1331

463 => (5 9) (9 7) (7 6)
0 9 => (5 9 9 7) (9 7 7 6)
30 + 39
69
5: 1
9: 3
7: 3
6: 1
Pascal's Triangle!!! sum=2**3 => 2**n-1
"5976"
"463"
"09"
"3902"
292 => (3 9) (9 0) (0 2)
11 => (3 9 9 0) (9 0 0 2)
3: 1, 9: 2, 0: 1
9: 1, 0: 2, 2: 1
21 + 11
32

1 3 3 1
actually: 1 2 1, 1 2 1
It grows with fibonaci at every step. n=1 splitted, n=2 C r, splitted
    n = 3Cr, etc.

Match.
Math. DP. Memoization.

Plan.
Note that number might get too large.
Do modulo as you go.
get first digit by looping from n - 2 combination r
    and summing and modulo to 

get next digit by doing the same loop, but from first digit.
TLE cos of math.comb. Time to find better way :)

3C0 3C1 3C2 3C3
1   3   3   1
1234567
1, 3, 6, 10, 15, 21, 28

1 3 3 1 => 2

1 4 6 4 1 => 3, 2

1 5 10 10 5 1 => 4, 5

1 6 15 20 15 6 1 => 5, 9, 5
64
62 => 31 31

1 7 21 35 35 21 7 1 => 6, 14, 14


2**n - i*2

nCR => nCr
Doing multiple too much
n! is computed too many times
n! / (n-r)!r!
Just compute r! that amount of times and store?
Nope! Don't store, just multiply (then divide) by i as you go.
e.g 4, 4! => 24
i =>  0  1 2 3 4
r =>  1  1 2 6 24
n-r=> 24 6 2 1 1
1
e.g 3! => 6
i =>  0 1 2 3
r!=>  1 1 2 6
n-r!=>6 2 1 1
"34789"
first = second = 0
N = 3
comb = 3

i = 1, => 3
needed = 3
first = (3 + 4 * 1) % 10 => 3
second = (4 + 4 * 1) % 10 => 4
+Optimization: Save combinations and reuse.

Implement.
""" 
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        first = second = 0
        N, comb = len(s) - 2, 1
        X = 1 + N // 2
        combs = [0] * X
        s = [*map(int, s)]
        for r in range(X):            
            combs[r] = comb % 10
            needed = combs[r]
            first = (first + s[r] * needed) % 10
            second = (second + s[r + 1] * needed) % 10
            comb *= (N - r) or 1
            comb //= (r + 1) or 1

        i = 2 - (N & 1)
        for r in range(X, N + 1):
            needed = combs[X - r - i]
            first = (first + s[r] * needed) % 10
            second = (second + s[r + 1] * needed) % 10

        return first == second


"""
Review.
3253285
578503
25353
7888
566
12

Evaluate.
Space: O(n)
Time: O(n)
"""