# from decimal import Decimal as D

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        number = x
        n = int(math.log10(x))+1

        for left in range(n-1, 0, -2):
            left_side = number // 10**left
            number %= 10**left

            right_side = number % 10
            number //= 10

            if left_side != right_side:
                return False

        return True


class Solution1:
    """Didn't work because of floating point arithmetic error"""
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        def get_digit(length, num, i):
            return int(math.modf(num / 10**(length-i))[0] * 10)
             
        n = int(math.log10(x))+1
        left, right = 0, n-1
        while left < right:
            # Number: x, length of number: n, position: left
            if get_digit(n, x, left) !=  get_digit(n, x, right):
                return False
            left += 1
            right -= 1
        return True

# Use two numbres. Number 
