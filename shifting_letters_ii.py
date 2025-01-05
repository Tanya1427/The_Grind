"""
Understand:
0 -> Backward
1 -> Forward
chr, ord

Match:
Prefix sum. String

Plan.
Brute.
Make a hash map (or array of len n) of shifts for each index.
For each start, end, loop through start -> end to 
 add/subtract number of shifts held in hash map.
Set new array
Loop through hash map to fill in array with previous values
 and shifts applied.

PlanA.
[[0,1,0],[1,2,1],[0,2,1]]

Can't lie. It's God who told me this one 🙌
Make an array of len(s)+1 fill with zeros, prefix_shifts.

You want to have a cummulative value of what you will be shifting each index with.
Consider the start and end in shifts.
loop through start, end, direction in shifts:
    shift = 1 if dir is 1 else -1
    increase prefix_shifts[start] by shift
    set prefix_shifts[end+1] to what will make the shift 0
    # That way, when the cummulative array is created from the prefix_shifts
    # The end point will be 0...
    # Actually, don't just SET prefix_shifts[end+1] to -shift
    increase prefix_shifts[end+1] by -shift sum
    # So that, if prefix_shifts[end+1] had a value before,
    # it will be updated accordingly
"""
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Create prefix_shifts
        n = len(s)
        prefix_shifts = [0] * (n+1)  # to allow end+1 setting.
        for start, end, direction in shifts:
            shift = direction or -1
            prefix_shifts[start] += shift
            prefix_shifts[end + 1] -= shift

        # Accumulate prefix_shifts using my usual method :)
        for i in range(1, n + 1):
            prefix_shifts[i] += prefix_shifts[i - 1]

        # Now increase character [i] by prefix_shifts[i], convert.
        ORD_A = ord('a')
        N_LOWER = 26
        new_string = [ord(ch) - ORD_A for ch in s]
        for i, letter_index in enumerate(new_string):
            new_string[i] = ascii_lowercase[
                (letter_index + prefix_shifts[i]) % N_LOWER]

        return "".join(new_string)

"""
Review.
[[0,1,0],[1,2,1],[0,2,1]]
s = "abc"
cumu_sum = 1
prefix_shifts
[0, 1, 1, -2]

prefix_shifts
[0, 1, 2, 0]

Evaluate:
n -> len(s)
Space: prefix_shifts, new_string => O(n)
Time: 3 to-n for loops: O(n)
"""