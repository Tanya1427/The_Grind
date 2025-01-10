"""
Understand:
26 lowercase. word[i] < 10. order doesn't matter

Match
String. Hashmap

Plan.
set hashmaps base_map and changing_map.
["leetcode"]
for word in words2:
    # changing map should be clear here.
    for character in word:
        If in base_map, add to changing_map instead.
    after additions for that word
    update base_map to max of what's in changing_map and itself.
    do this while clearing changing_map for the next word
E.g
words2 =
["le","llee", "elee"]
base_map=>{
    'l': 1->2->2,
    'e': 1->2->3,
}
for word in words1:
    clear changing
    get word count:
    compare changing with base_map.
        add to answer if valid

>> answer

"""

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        base_map = defaultdict(int)
        changing_map = defaultdict(int)
        answer = []
        # Loop through words2 to make a count of all chars.
        # As if they were one word.
        for word in words2:
            checked = False
            for ch in word:
                changing_map[ch] += 1

            while changing_map:
                ch, count = changing_map.popitem()
                base_map[ch] = max(base_map[ch], count)  # if ch not in base_map, base_map[ch] is 0 so count works

        # The changing_map is clear after last while loop: {}
        # Now, the changing_map will be used to count chars in words1
        # Get the count of words in words1 and compare with base_map
        for word in words1:
            for ch in word:
                changing_map[ch] += 1

            for ch, count in base_map.items():
                if ch not in changing_map or changing_map[ch] < count:
                    break
            else:
                answer.append(word)

            changing_map.clear()

        return answer

"""
Reviewed

Evaluate:
Space: O(1). base_map and changing_map max_len == 26
Time: O(n), words[i] length is minimal <= 10
"""