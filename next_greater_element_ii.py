"""
Understand.
The largest element(s) won't have a next greater element.
circular means that nums[n] is nums[0], essentially mod n.

Match.
Monotonic stack.

Plan.
init stack
init result[array length]
From the back of the array
    if stack is empty:
        set result of position to -1
    if last element in stack is greater than current element
        set result of position to last element in stack
    else:
        set to -1
        pop until greater
    add current element

stack will contain nums reversed in monotonic order.
Assuming continuation. I.E. after the array ends at the front
from the back of the array, do until element is maximum
    return result if stack is empty
    if stack top is greater than current element:
        set result of position to top
    else:
        pop stack until greater than current element
        - no adding anymore.
if element is maximum, everything has been fixed (except it)
stack will exhaust if it encounters maximum I believe
if stack exhausted, return

Implement.
note from code: mstack need to be stack? or can just be array with poitner?
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        mstack = [nums[-1]]
        n = len(nums)
        res = [-1] * n
        fixed = [False] * n
        for i in range(n - 2, -1, -1):
            while mstack and mstack[-1] <= nums[i]:
                mstack.pop()

            if mstack:  # last element will be greater if it exist
                res[i] = mstack[-1]
                fixed[i] = True

            mstack.append(nums[i])

        for i in range(n - 1, -1, -1):
            if fixed[i]:
                continue

            while mstack and mstack[-1] <= nums[i]:
                mstack.pop()
            
            if not mstack:
                break

            res[i] = mstack[-1]
            fixed[i] = True

        return res


"""
Review.
- with elements all the same
- with sorted in ascending
- with n = 1, n=2
Failed first submit
[1,5,3,6,8]
[8,6,5]
[5,6,6,8,-1]
- error involving setting after pops... fixed.
- error involving using -1 to check ... "fixed"

Evaluate.
Space: O(n) for stack
Time: O(n) for looping twice (max)
"""
