"""
UMPIRE:
Understand:
I understand.
Match.
Prefix sum.
Plan.
label strings 1/0 for vowel or not
["aba","bcb","ece","aa","e"]
   1     0     1     1   1
   1     1     2     3   4

Get the range query.
Implement:
"""
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_count = [{word[0], word[-1]}.issubset(vowels) for word in words]
        prefix_sum = vowel_count.copy()
        for i in range(1, len(words)):
            prefix_sum[i] += prefix_sum[i - 1]
        return [
            prefix_sum[end] - prefix_sum[start] + vowel_count[start]\
             for start, end in queries
        ]
"""
Reviewed.
Evaluate:
Space: O(n) -> n is length of words
Time: O(|queries| + n) 
"""