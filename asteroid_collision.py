"""
Understand
+ -> right
- => left
|A| => size
What sign is 0???

IF two of different signs meet, |bigger| one remains to colide with the next.
Asteriod of len 1 will just keep moving

Understood wrongly... It's a MEDIUM, Daniel :)
Start from front - assume asteroids are sent from first to last

current next,
if current is positive -> and next is negative <-, then they will colide.

Match.
Stack

Plan:
Set deleted to 0 and move on.
Decide whether asteroid explodes - set to OUT if it does,
move on.
OUT = 0
I guess I could use two pointers to keep track of next and current.
current, next => pointers
if current and next are equal,
    set both to OUT
    decrease current
    increase next
if current is greater:
    set [next] to OUT
    increase next

if signs become the same
    increase both next and previous.

The above approach is, well...
Kinda cool that this came to me today: (a < 0) ^ (b < 0) => different signs

Hinted approach :)
create a new array stack.
stack should be asteroids[0]
keep adding asteroids and determine what will happen.
will have sth like while the one to be added is negative and the top of stack is positive
Implement:
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for new in asteroids:
            # Empty || Last asteroid moving left || Both moving same direction (right in this case)
            if not stack or stack[-1] < 0 or new > 0:
                stack.append(new)
                continue

            # Initially, stack[-1] should be positive, new should be negative. Instead of abs, how about -
            while stack:
                # Same direction, left. None explodes.
                if stack[-1] < 0:
                    stack.append(new)
                    break

                # last must be positive here, explode it.
                last = stack.pop()
                
                # They are equal, the new explodes
                if last == -new:
                    break
                
                # The last beat the new, explode the new, reform the last :)
                if last > -new:
                    stack.append(last)
                    break

            # new kept exploding the last. First statement handles A LOT :)
            if not stack and -new > last:
                stack.append(new)

        return stack




"""
Reviewed

Evaluate:
Space: O(n) -> worst case
Time: O(n)
"""
