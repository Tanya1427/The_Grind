"""
Understand:
Palindrome starts and ends with the same letter
three - only one letter is not start/end
Subsequence counted only once - first and last occurences needed only.
s.length >> 10**5. Solution MUST be less than O(n-squared)

Match:
Hash set, table.

Plan.
Get first and last indices of unique chars in s.
0  1  2  3  4  5  6  7  8  9  10
a  n  b  a  d  v  e  b  f  a  j
=> {
    a: [0, 9],
    b: [2, 7],
    d: [4],
    n: [1],
    v: [5],
    e: [6],
    f: [8],
    j: [10],
}
a: ana, aba, aaa, ada, ava, aea, aba, afa => aba appear twice!
Problem: get unique characters between indices i and j
Actual problem: Get NUMBER of unique characters between indices i and j

Solution: Save number of unique characters from 0 -> n
            i.e generate "prefix_count" of numbers
            use for each first and last index of every character :)

0  1  2  3  4  5  6  7  8  9  10
a  n  b  a  d  v  e  b  f  a  j

Implement:
"""
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Get number of unique characters from 0 -> any n
        # Get first and last indices of unique chars
        # In one pass
        n = len(s)
        char_count = Counter(s)
        unique_chars = set()
        unique_from_0 = []
        is_unique = []
        unique = 0
        first_last = defaultdict(list)
        for index, ch in enumerate(s):
            is_unique.append(int(ch not in unique_chars))
            unique += ch not in unique_chars
            unique_chars.add(ch)
            unique_from_0.append(unique)
            if len(first_last[ch]) == 2:
                first_last[ch][1] = index
                continue
            first_last[ch].append(index)

        # print(first_last)
        # print([*range(n)])
        # print(unique_from_0)
        # print(is_unique)
        # Get n unique chars between each first last
        n_subsequence = 0
        for first, last in filter(lambda x: len(x) == 2, first_last.values()):
            diff = unique_from_0[last] - unique_from_0[first]
            n_subsequence += diff + 1
            # n_subsequence += char_count[s[last]] > 2
        return n_subsequence

"""
Plan:
Brute force:
get first and last indices.
For each of those that have first and last, get number of unique chars between
 first and last
total is answer

Implement
"""
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Get first and last indices of each ch.
        # For those that have first and last,
        # - get number of uniques between them
        n = len(s)
        first_last = defaultdict(list)
        for index, ch in enumerate(s):
            if len(first_last[ch]) == 2:
                first_last[ch][1] = index
                continue
            first_last[ch].append(index)

        n_subsequence = 0
        for first, last in filter(lambda x: len(x) == 2, first_last.values()):
            unique_chars = set()
            for i in range(first+1, last):
                n_subsequence += s[i] not in unique_chars
                unique_chars.add(s[i])
        return n_subsequence

"""
Reviewed
Evaluate:
Time: O(26*n) (max=26 if all a-z has first and last index) => O(n)
Space: O(26*3), key, first, last for all a-z => O(1)

Todo: Modify the prefix sum approach above so that it works for all test cases.
"""