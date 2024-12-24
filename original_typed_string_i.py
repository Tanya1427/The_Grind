"""
Understand:
"At most once"
No need for combinations
aaabbb => aaab, aaabb, aaabbb, abbb, aabbb, aaabbb

Match:
Math. Loop(holes)

Plan
(sum of frequency of all letters i.e len of string)
 - (number of unique chrs)
 + (1 i.e. the original)

Explanation? Well... The characters with freq of 1 
 do not have any "possible string"
 freq of 2, 1 other possible string.
 .... of 3, 2 other possible strings...
 .... of 4, ... you get where I'm going.
For one letter/character, we have freq(letter) - |letter| (1)
And then the original string

Flaw in plan: ere, haha. You get...

Plan B:
(There's probably an easier way)
Have a running 'counter'
it will count two things.
1. Frequency of 'running' characters.
2. Amount of 'running' characters.

i.e. loop that counts how many times it 'switches'
and also counts how many times it stays in a switch.

Actually...
The sum of the counts of how many times it stays in a switch 
 is strlen!. So just count how many switching there are.

Implement
(initial, failed in 'ere')
class Solution:
    def possibleStringCount(self, word: str) -> int:
        return len(word)-len(Counter(word))+1

"""
class Solution:
    def possibleStringCount(self, word: str) -> int:
        switch_count = 0
        letter = ""  # Will cause first switch
        for ch in word:
            switch_count += ch != letter  # To switch or not to
            letter = ch
        return len(word)-switch_count+1

"""
Reviewed.
Evaluate:
Space: O(1)
Time: O(n) for loop (no pun intended ('for')).
"""
