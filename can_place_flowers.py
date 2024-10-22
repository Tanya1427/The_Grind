"""
Understand:
[1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0]

The best should be when the 1s and 0s are strictly switching.

What if  there are two choices.

[0, 0, 0, 0, 0]
=> [1, 0, 1, 0, 1]
=> [0, 1, 0, 1, 0]

Try the two? Will there ONLY be two?
Is there a way to determine if there'll be two - there is!
If it starts with two 0s, there are two choices if the third is 0
=> Plan x.

Match.
Array. Greedy.

Plan.
get the max you can put. return max >= n
It's greedy.
Using index i, if i is 0, and if i-1 and i+1 is 0, increment max and 
increment i by two.
Ignore ones as you move, always moving to the next 0.
Is this effective?

x.
Just check for the two boundaries! A good way will be to add zero to the front 
and back of the list :)
Then start from index 1, not index 0.

Implement
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Sorry about my use of boolean as integers - might cause confusion, but True => 1, False => 0
        max_count, i, length = 0, 0, len(flowerbed)
        while i < length:
            add = not ((i > 0 and flowerbed[i-1])+flowerbed[i]+(i < length-1 and flowerbed[i+1]))
            max_count += add
            i += 1+add
        return max_count >= n

"""
Reviewed

Evaluate:
Space: O(1)
Time: O(n). n/2 in best case is still O(n)
"""
