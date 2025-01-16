"""
Understand:
XOR is cummutative+associative. A XOR 0 is A. A XOR A is 0
[2, 1, 3]
[10, 2, 5, 0]

One pairing
[8, 0, 7, 2, 11, 3, 4, 1, 9, 1, 6, 3]
The pairing order does not matter.

Check distributiveness of XOR
is a ^ (b ^ c) == (a ^ b) ^ (a ^ c)? Nah.
but a ^ (b | c) == (a ^ b) | (a ^ c). Cool, but not the point.
Point is that the order doesn't matter. Cummutative AND associative.

Made some testcases and noticed an 'anomaly'
Some inputs did not depend on nums1 values... so...

Match.
Bit wisdom.

Plan.
take nums1 = [i1, i2, i3, i4...]
nums2 = [j1, j2, j3, j4...]

The paring for all in nums1 to all in even len(nums2)
first one:
i1 ^ j1, i1 ^ j2, i1 ^ j3, i1 ^ j4. Rearrange.
i1 ^ i1 ^ i1 ^ i1 ^ j1 ^ j2 ^ j3 ^ j4
0 ^ XOR(nums2), see?
All => 0 ^ XOR(nums2) ^ 0 ^ XOR(nums2) ... rearange => 0 ^ 0 ^ 0... ^ XOR(nums2) ^ XOR(nums2) ...
if len(nums1) is odd, return XOR(nums2) else 0
Do for odd len(nums2).
first one = i1 ^ j1, i1 ^ j2, i1 ^ j3 Rearrange.
i1 ^ i1 ^ i1 ^ j1 ^ j2 ^ j3
 = i1 ^ XOR(nums2)
=> i1 ^ XOR(nums2) ^ i2 ^ XOR(nums2) ^ i3 ^ XOR(nums2) ...
Rearrange
i1 ^ i2 ^ i3 ... ^ XOR(nums2) ^ XOR(nums2) ^ XOR(nums2)....
==> XOR(nums1) ^ (0 if len(nums1) is even else XOR(nums2))
[for all==ix] ^ XOR(nums2) => XOR(nums1) ^ XOR(nums2)

Now plan.
save len_2 = len(nums2)
xor_2 = XOR(nums2)

if len_2 is even, xor(ix, ix, ix, ...) is 0
    return xor_2
# else
len_1 = len(nums1)
xor_1 = XOR(nums1)
return xor_1 ^ (xor_2 * (len_1 & 1))

Write code to wait before computing XOR(nums1)

Implement.
"""
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        len_2, len_1 = len(nums2), len(nums1)
        xor_2 = 0
        for j in nums2:
            xor_2 ^= j

        if not len_2 & 1:  # For the sake of having less nested code
            return len_1 & 1 and xor_2

        xor_1 = 0
        for i in nums1:
            xor_1 ^= i

        return xor_1 ^ (len_1 & 1 and xor_2)

"""
Reviewed.

Evaluate.
n, m = len_2, len_1
Space: O(1)
Time: O(n + m)
"""