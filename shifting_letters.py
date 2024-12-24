"""
Match:
Reverse cummulative sum.
"""

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        A = ord('a')
        answer = [""] * n
        shift = 0
        for i in range(n - 1, -1, -1):
            shift += shifts[i]
            answer[i] = chr(A + (shift + (ord(s[i]) - A)) % 26)
        return "".join(answer)

"""
Evaluate.
Space: O(1) OR O(n) for returned value
TIme: O(n)
"""
