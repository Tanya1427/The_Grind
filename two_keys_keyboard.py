"""
Understand:
change only a count variable.

Two operations: Copy, Paste
Starts with 'A'

do for n=6
'A'
board = 'A'
paste_hold = ""
1. Copy (nothing to paste :) )
board = 'A'
paste_hold = 'A'

2. Paste
board = 'AA'
paste_hold = 'A'

3. Paste
board = 'AAA'
paste_hold = 'A'

4. Paste
board = 'AAAA'
paste_hold = 'A'

5. Paste
board = 'AAAAA'
paste_hold = 'A'

6. Paste
board = 'AAAAAA'
paste_hold = 'A'

return 6
 
Match:
DP

Plan:
Must CopyAll the first time. Must paste last time
Must not CopyAll twice.
Copy will set paste to board_count

Board will not be actually copied - numbers will be used.
THINK
branch.
copying => paste = board
pasting => board += paste
checking => if board == n.
# Start by copying
copying == 0, pasting == 1
operations = 1  # Copied
last_operation = 0
paste = 1
board = 1

Use recursion...
def keyboard(paste, board, last_operation, operations):
    if board == n:
        return operations
    elif board > n:
        return False
    if last_operation == 0:  # A copy.
        # paste
        return keyboard(paste, board+paste, 1, operations+1)
    # last operation was pasting
    # I can decide to either copy or paste
    # But I must return the minimum between the two options I chose
    # I must do each option
    copied = keyboard(board, board, 0, operations+1)
    pasted = keyboard(paste, board+paste, 1, operations+1)

    return min(copied, pasted)



"""
class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        COPIED = 0
        PASTED = 1

        def keyboard(paste, a_count, last_operation, operations):
            if a_count == n:
                return operations
            elif a_count > n:
                return float("inf")  # min will never return this, hopefully :)
            
            if last_operation == COPIED:
                # PASTE
                return keyboard(paste, a_count+paste, PASTED, operations+1)
            # PASTED
            return min(
                keyboard(a_count, a_count, 0, operations+1),  # Value from copying
                keyboard(paste, a_count+paste, PASTED, operations+1)  # Value from pasting
            )

        a_count = 1  # Start of notepad
        last_operation = COPIED  # Must be first operation
        operations = 1  # Copied A
        paste = 1  # Paste value now has something

        return keyboard(paste, a_count, COPIED, operations)

"""
Reviewed:
Passed all leetcode testcases

Evaluate:
Next to do before finding optimal
"""
