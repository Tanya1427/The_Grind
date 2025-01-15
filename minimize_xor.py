"""
Understand:
num1, num2, x. numi max == 10**9 -> Look for less than O(log n)/O(1)
num2.bit_count() == x.bit_count() == l
n = num1.bit_length

must be up to n in length. must be up to l in length too.

Match.
Bit Manipulation.

Plan.
set the x to binary string of 1111... having length of num2's bitcount
if len(num1) > len(x):
    shift x to same size

The way will be to move through from higher place values to lower.
Since it helps to reduce the XOR value when higher place values resolve to 0

nth = bitlength min(num1 | num2)
i = n+1
j = 1
while i:
    n -= 1
    num1[i] will be 1 at first...
    num, v = num1[i], x[i]
    if num = v:
        # Perfect. Continue.
    
    # Not equal
    if v == 1:  # num is 0...
        change x in two places.
        x_copy = x
        j = 1
        rem = 1
        stop = false
        while rem:
            rem = x_copy & 1
            x_copy >>= 1
            j += 1
            if j >= i:
                stop = true
                break
        if stop:
            continue  # Should not unset x[i] if it cannot be set.

        set x[i] to 0  # Can set and unset
    else:
        maybe just make the if v==1 code able to cover this too )

return x

Implement.
"""
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        len_x, n = num2.bit_count(), num1.bit_length()
        x = 2**len_x - 1 << (n - len_x) * (n > len_x)

        i = n
        while i:
            i -= 1
            # Create `checker` to check if ith bit is set/not
            checker = 2 ** i
            num, v = num1 & checker, x & checker
            if num == v:
                # XOR will be minimal if both are set.
                continue
            
            # Depending on what v is,
            #  check if should set or unset x
            # Move j to where it will set something equal
            # If v == 0, to 0 in x, 1 in num1. if can't find...
            # IF v==1 to 1 in x, 0 in num1. Be greedy.

            # First make v 1/0
            v >>= i
            x_copy, j, rem = x, -1, v
            while rem == v:
                rem = x_copy & 1
                x_copy >>= 1
                j += 1
                if j >= i:
                    break
            else:
                # switch x[i] using XOR (^)
                x ^= checker
                # switch x[j] also
                x ^= 2 ** j

            # No need, really. It will continue till it stops if.
            if x == num1:
                return x

        return x

"""
Reviewed.

Evaluate:
Space: O(1)
Time: O((logn)**2)
"""