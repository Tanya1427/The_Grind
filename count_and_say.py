"""
Understand.
n max is 30. Space ignorant solution could work.

Match.
DP? Hash map. Counting. deQue

Plan.
(prolly not the most optimal...)
rle = ['1'] (deque)
while n:
    current = last of rle
    count = 0
    do len rle times:
        # go through rle
        next = pop rle
        if next is current
            add to count
        else or no rle empty
            add current to start of deque
            for ch in reverse count:
                add to deque
    n --
return "".join(deque)

Implement.
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        rle, n = deque('1'), n - 1
        while n:
            current, count = rle[-1], 0
            for _ in range(len(rle)):  # range is computed only once
                nextt = rle.pop()
                if current == nextt:
                    count += 1
                    continue
                rle.appendleft(current)
                rle.appendleft(str(count))
                current, count = nextt, 1

            rle.appendleft(current)  # DRY :(
            rle.appendleft(str(count))

            n -= 1
        return "".join(rle)

"""
Review.
Ran on custom testcases. Seems like there's a 123 pattern.
There might be a way of harnessing the pattern.
Count won't get too big - no need to do reverse adding

Evalaute.
n is average length of RLE.
Space: O(output). Maybe O(n**2) - counting and adding the count.
Argue O(1) - output doesn't count :)
Time: O(n**2) - Looping the count.

"""
