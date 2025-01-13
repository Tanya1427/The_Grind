"""
Understand.
String length will reduce by 2 for every process
count of the "processed letter" will also reduce by 2.

0 1 2 3 4 5 6 7 8  2, 0|3   0 1 2 3 4 5 6  3, 0|5   0 1 2 3 4
a b a a c b c b b  2, 0|3   b a c b c b b  3, 0|5   a c c b b

You can not proceed if count of a letter is less than 3.

Match.
Counting. HashMap

Plan.
The Understanding phase of this was EXTREMELY helpful!
There's no way the strings can be entangled that will stop this,
now Plan:
Counter -> You can use [0] * 26 if you want. Counter.values() for 
count == count of a letter.
final_count = 0
if count > 2, "remove 2 until it is less than 2"
    # Do this with math.
    if 3, -2 => 1. if 4, -2 => 2. if 5, -2 => 3 => 1.
    There are only two ways. If odd: 1, if even: 2
    remember, count & 1 is 1 if odd, 0 if even
    use 2 - (count & 1)
    add count to final
else 
    add count to final

From first thought.
return sum(2 - (count & 1) if count > 2 else count for count in Counter(s).values())

Second thought.
Actually, check what's not greater than 2
1 and 2 (strlen can't be 0)
2 - (1 & 1) => 2 - 1 => 1 || 2 - (2 & 2) == 2 - 0 => 2
Ah! No need for condition!


Implement
"""
class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(2 - (count & 1) for count in Counter(s).values())

"""
Reviewed

Evaluate:
Space: O(1) for 26 letters max count
Time: O(n) for creating counter and looping in sum
"""