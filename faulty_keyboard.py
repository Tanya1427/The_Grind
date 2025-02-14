"""
Understand.
mierogliphics
 0    1     2   3
[m, erogl, ph, cs] -> n = len(_)
201
3102

if n is even, start with appendleft, else start with append
if n is even, positions will start with even up to 0, else start with odds
6 -> 6 4 2 0 1 3 5
7 -> 7 5 3 1 0 2 4 6

7 5 3 1 0 2 4 6


Match.
Deque.

Plan.
form groups of splitted s with 'i'. n = len(groups)
last = groups.pop()

result = [""] * n
index = 0
incr = -2
final_pos = n - 2
Add the first indices to the result, reversed
final_pos = abs(final_pos + 1)
add the rest after resetting, without reversing

```Might be tempting to use 1 while loop with a condition)
   imo, twill use more operations for checking
```

Implement.
"""
class Solution:
    def finalString(self, s: str) -> str:
        groups = s.split('i')
        n = len(groups)
        final_pos = n - 2
        index = 0
        result = [0] * n
        while final_pos >= 0:
            result[index] = groups[final_pos][::-1]
            index += 1
            final_pos -= 2
        final_pos = abs(final_pos + 1)  # Reset
        while index < n:
            result[index] = groups[final_pos]
            index += 1
            final_pos += 2
        return "".join(result)

"""
Reviewed.

Evaluate:
Space: O(n), for groups, for values from slices.
Time: O(n).

Better way, use a loop to gather letters,
  switch between adding to front or back when 'i' is encountered.
"""