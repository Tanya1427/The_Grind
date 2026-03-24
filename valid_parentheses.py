# UMPIRE
"""
Understand.
1. Problem statement. 25%

2. Checking, and making examples. 40%
()()()()
([]])(}())()
[]{
((({{{{{{{{[[[[[[[[[[((((((((((((((((((((((((((((((((((((((((((((((((((((((

3. 35%
Checking/asking for constraints.

Match.
Stack.

Plan.
([]{})
make map of parenthesis
) -> (;
] -> [;
} -> {;

init stack[]
go through brackets
    if it's a type of open parenthesis:
        push to the stack
    if it's a closed
        if stack is empty:
            return False
        can this close reslove open bracket type?
            if no:
                return False

if stack is empty:
    return True
else: return False

Implement.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        can_close = {"}":"{", ")":"(", "]":"["}
        open_parentheses = set(can_close.values())
        stack = []
        for parenthesis in s:
            if parenthesis in open_parentheses:
                stack.append(parenthesis)
                continue

            if not stack:
                return False

            if can_close[parenthesis] != stack[-1]:
                return False

            stack.pop()

        return not stack

"""
Review.
Starts with closed parenthesis
Has no closed parenthesis
IS different

Evaluate.
where n is the length of `s`
Space: Worst case, no popping: O(n)
Time: O(n)
"""
