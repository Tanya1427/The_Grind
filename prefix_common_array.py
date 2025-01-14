"""
Understand:
A, B n
C C[i] == count of commons from 0 to i (inclusive) in A and B
C[0] 0 if A[0] != B[0], C[-1] always n. n max => 50...
COUNT.

Match:
Two pointers? Hash map?

Plan.
Brute.
[1, 3, 5, 4, 2]
[3, 1, 2, 5, 4]

i=0, C[i] = 0, first = {1}, second = {3}
i=1, C[i] = 2, first = {1, 3}, second = {3, 1}
i=2, C[i] = 2, first = {1, 3, 5}, second = {3, 1, 2}
i=3, C[i] = 3, first = {1, 3, 5, 4}, second = {3, 1, 2, 5}
AHA moment :) No more brute force!!!

Traverse both, add when count of any gets to 2 :)
  The count can never be more than 2 for any...

Plan.
Use a set. Or array counted/common.
set C = [0] * n, i=0  # You can use append too
common_count = 0
loop though a, b simulataneously:
    for x in (a, b):
        if x in set or array[x-1|x]:
            common_count += 1
        else:
            set.add(x) or array[x-1] = 1

        C[i] = common_count  # 
        i += 1
Using an array is better tracking in my opinion. Set will hash and add and stuff.

Implement.
"""
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n, i, common_count = len(A), 0, 0
        # 1 extra spot is probably better than n -(minus) operations :)
        counted = [0] * (n + 1)
        common = [0] * n

        for a, b in zip(A, B):
            for x in (a, b):
                if counted[x]:
                    common_count += 1
                    counted[x] = 0
                else:
                    counted[x] = 1
                common[i] = common_count
            i += 1

        return common

"""
Reviewed.

Evaluate:
n = input size
Space (not counting return): O(n) for counted check.
Time: O(n) for looping through both.
"""