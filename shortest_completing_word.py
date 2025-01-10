"""
UMPIRE
Understand.
licencePlate and words
 "1s3 PSt", words = ["step","steps","stripe","stepple"]

licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
s => pest.

Match.
HashMap. String.

Plan/Pseudocode.
Make hash map from the license plate.
    smalletters: count.

min_length = 0
answer_index = 0

for each word in words:
    copy the hashmap.
    loop through ch in words:
        if ch in hashmap:
            hashmap[ch] -= 1
            if hashmap[ch] < 0:
                dont' coutn in.


Implement
"""

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        base_hashmap = defaultdict(int)
        for ch in licensePlate:
            if ch.isalpha():
                base_hashmap[ch.lower()] += 1

        min_len = float("inf")
        answer_index = 0
        for i, word in enumerate(words):
            hashmap = base_hashmap.copy()
            for ch in word:
                if ch in hashmap:
                    if not hashmap[ch]:
                        continue
                    hashmap[ch] -= 1

            if not sum(hashmap.values()) and len(word) < min_len:
                answer_index = i
                min_len = len(word)

        return words[answer_index]
"""
Reviewed

Evaluate.
Space: Hashmap, O(n) -> repeated hashmap copies for all words
Time: O(n * m). m = len(words[i]) | n = len(words)
"""