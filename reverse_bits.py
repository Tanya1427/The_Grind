"""
UMPIRE
Understand
102

1100110
00000000000000000000000001100110
01100110000000000000000000000000

0110011 * 10000000000000000000000000
result_ * 2**25

102

100 + 2
25*4 + 2
(16+9)*4 + 2
(2**4+9)*4 + 2

 10 => 2
100 => 4
1000 => 8
100000 => 32

32-7=>25
00000000000000000000000001100110
01100110000000000000000000000000

2**25

Match:
Bit manipulation. Math.

Plan/Pseudocode.
102 => 1100110
get bit_length = 7

subtract from 32 => 32 - 7 => 25

reverse the bits of number
0110011

43 => 101011
43 => 110101
110101
110000 48
+  100 4
+    1 1
53

bin(43) = "0b101011"
"101011"[::-1] => "110101" => 53 * 2**26

multiply by 2**subtraction

43
43 / 2 => 21 r 1
21 / 2 => 10 r 1
10 / 2 =>  5 r 0
 5 / 2 =>  2 r 1
 2 / 2 =>  1 r 0
 1 / 2 =>  0 r 1

0
0*2 + 1 => 1
1*2 + 1 => 3
3*2 + 0 => 6
6*2 + 1 => 13
13*2 + 0=> 26
26*2 + 1=> 53

43 => 110101 => 53

Implement:
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        power_of_2 = 32 - n.bit_length()
        reversed_number = 0
        while n > 0:
            rem = n % 2
            n //= 2
            reversed_number = 2*reversed_number + rem
        return reversed_number * 2**power_of_2

"""
Review/Run
2, 209923840982, 43

Evaluate:
Big O    => Worst case.
Little O => Best case
"Average" O => Average case
Space:  => O(1)

8 => 3: 4, 2, 1
242 => 121, 60, 30, 15, 7, 3, 1 => 7
log2()
Time: O(log n)

[1,2,3,4,[5,6,7,[8,9] => log2(n)
"""
