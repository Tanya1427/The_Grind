"""
Understand:
DONT COPY/SLICE THE STRING

Match:
String. Two Pointers

Plan:
two pointers. When I pressed,
reverse array from start up to i's location.

IMPLEMENT
"""

class Solution:
    def finalString(self, s: str) -> str:
        typed = []
        for ch in s:
            if ch != 'i':
                typed.append(ch)
                continue
            start, end = 0, len(typed)-1
            while end > start:
                typed[start], typed[end] = typed[end], typed[start]
                start += 1
                end -= 1

        return "".join(typed)

"""
seneledan
Reviewed

abcdeighk
  2
abcde
ebcda
edcba
edcba[]

Evaluate.
Space: O(n)
Time: O(n)

"""
