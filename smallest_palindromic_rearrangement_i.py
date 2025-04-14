"""
Understand.
A palindrome must have characters having with count except maybe one character.
s.length max is 10**5. lowercase means no space except return value
s itself is palindromic
 (This helps to get the middle character needing to get the one with odd count)
P.S. This was April 12, 2025 contest question 2 ended (11pm CST).
But I only noticed, that the palindromic nature of the input helps if strlen is odd

Match.
Counting.

Plan.
get string len, make string builder with that, get count of letters sorted
if string len is odd, the palindrome must have that as a middle.
set the middle of the string builder, reduce the count for that character
    , and remove that entry in the dict/hashmap if it's count is 0

iterate over the count keys. keeping the index, i
reduce the counts while adding to the back and front of the stringbuilder

return the stringbuilder joined.

Plan.
Instead of using a stringbuilder, why not use a deque?
Might be faster as while loop not needed.
just .append(count[...]//2 * c) and .appendleft the same thing
Sorting will have to be reversed.

Implement.
"""

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        min_pal = deque()
        count = dict(sorted(Counter(s).items(), reverse=True))

        if n & 1:
            mid = s[n // 2]
            min_pal.append(mid)
            count[mid] -= 1
            if not count[mid]:
                del count[mid]

        for ch, freq in count.items():
            string = ch * (freq // 2)
            min_pal.append(string)
            min_pal.appendleft(string)

        return "".join(min_pal)

"""
Review.
When n is odd || when strlen is 1

Evaluate.
Note that `count` takes constant space
Space: O(1) ? Not really really. string is gabage collected
Time: O(n) for counting.
c * (count[c] // 2) doesn't really reduce Time Complexity
It helps though.
"""
