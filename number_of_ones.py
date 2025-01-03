"""
Understand:
n, n-1, ... 1
return value is usually > 0

Match:
Math.

Plan:
Get 1's in units, in tens, in 10**n's
13 => [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
       1   1    2   1  0  0  0  0  0  0  0  0  1
6

100 => 100, 91, 81, ... 21, 11, 1
1 -> 100
01, 11, 21, 31, 41, 51, .. 10
10, 11, 12, 13, .... 10
100 ... 1

|n|==3

1000 =>
9 + 90 + 


01, 11,  21,  ... 91  => 10

(1-9)(1-9)01 =>
11
21
31
..
91

101, 201, ... 901 => 9
111, 211, ... 911 => 9
121, 221, ... 921 => 9
................. => 9
191, 291, ... 991 => 9

9*10

10, 11, ... 19 => 10 || 100

(1->9)10 => 9
(1->9)11 => 9
(1->9)12 => 9
(1->9)13 => 9
(1->9).. => 9
(1->9)19 => 9
9*10 => 90

110, 210, ... 910 => 9
111, 211, ... 911 => 9
112, 212, ... 912 => 9
113, 213, ... 913 => 9
114, 214, ... 914 => 9
115, 215, ... 915 => 9
.....
119, 219, ... 919 => 9


9*10
100, 101, 102, .., 199


10000 > 7649 < 1000

1000 => 301

2000

1000 + 999 => 301
1999 + 1998 ... => 1000

7000 => 7 * (1000) + 1000
600 => 6 * (100)
40 => 4 * (10)
9 => 9 * (1)

100
1 + 10 + 10

1000
(10 + 9*10) + (10 + 9*10) + (100) + (1)
100 + 100 + 100 + 1 => 301

log(n) + 1

log(100)+1

10000
(1 + 9 + 9*10 + 9*9*10) + (10 + 9*10 + 9*9*10) + (100 + 100*9) + (1 + 9) + (1)
# 2831
1 + 1*9 + 10*9 + 100*9 => units
10 + 10*9 + 100*9 => tens
100 + 100*9 => hundreds
1000 => thousands
1
log(n) + 1 ========= n | 10

4001
(1, 10, 90, 810)

n|10 n*log(n) + 1

10**n. !10**n. coding.

Implement:
"""

class Solution:
    def countDigitOne(self, n: int) -> int:
        return int(n/10 * log10(n) + 1 ) if n else 0

