"""
Understand.
len(stack) & 1, return False

Match.
Stack. Greedy.

Plan.
start stack = []
n = len(s)
loop i through range(n):
    if not stack: # You can't add a ')' first:
        if s[i] is )
            if is locked:
                return False
            else: add('(') to stack.
            continue
    if s[i] == (
        add to stack
    else: )
        pop from stack (stack is not empty at this point)
return not stack
Question: Is there a time when you'd need to change s[i] to ')'?

PlanB.
Follow the hint. Hint one hints that you go by two :)

) ) ) ) ) )
0 1 1 1 0 0
I mistakenly hit ctrl+enter (:

PlanC, C==Copilot.
# Explanation:
# - The first pass ensures you have enough open parentheses to balance closing ones.
# - The second pass ensures the reverse, verifying from the end of the string.
# - Using max and min counters tracks the range of valid balances at each step.

Quite the solution - in my opinion!

Implement:
"""
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n & 1: 
            return False

        # Left to Right Scan
        min_open, max_open = 0, 0
        for i in range(n):
            if s[i] == '(' or locked[i] == '0':
                max_open += 1
            else:  # is ')', closed bracket, and can't be changed
                max_open -= 1
            
            if s[i] == ')' or locked[i] == '0':
                min_open -= 1
            else:
                min_open += 1
            
            if max_open < 0:
                return False
            min_open = max(min_open, 0)
        
        # Right to Left Scan
        min_open, max_open = 0, 0
        for i in range(n - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                max_open += 1
            else:
                max_open -= 1
            
            if s[i] == '(' or locked[i] == '0':
                min_open -= 1
            else:
                min_open += 1
            
            if max_open < 0:
                return False
            min_open = max(min_open, 0)
        
        return min_open == 0

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n & 1: return False
        if s[0] == ')' and locked[0] == '1': return False
        stack = 0
        for i in range(1, n, 2):  # Will end in odd i
            if s[i] == ')':
                if s[i - 1] == '(' or locked[i - 1] == '0':
                    continue
                if not stack:
                    return False
                # s[i - 1] is ')' and it's locked, and can't pop
                stack -= 2
            # s[i] == '('
            if s[i - 1] == '(':
                if locked[i] == '0':  # Change and pop()
                    continue
                stack += 2  # Add two open brackets
            else:  # s[i - 1] == ')'
                if locked[i - 1] == '0':
                    stack += 2
                elif locked[i] == '0':
                    stack -= 2
                    if stack < 0:
                        return False

        return stack == 0

"""
Review
( ( ( ) ( ) ) )
1 1 1 0 1 0 0 0

(((
```
Evaluate:
Space: O(1) -> no-stack.
Time: O(n)
"""