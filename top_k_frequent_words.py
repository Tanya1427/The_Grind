"""
U_MPIRE
Understand.
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]

words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]

words = ["a", "a", "b"] k = 5

["aAR", "AAR"]
Constraints.

words = ["hat", "cat", "hat", "hat", "bat", "dat"] k = 3
output: ["hat", "bat", "cat"]

words = ["cake","ice","cake","apple","ice","apple","juice","juice"] k = 3
output: ["apple", "cake", "ice"]

word=["cart", "bart", "mart", "dart", "cart", "part", "bart"] k = 4
output: ["bart", "cart", "dart", "mart"]

word = ["word"] k = 1
output = ["word"]

Match.
Counting | Hashmap. Heaps. Sorting.

Plan.
1st Plan: Sorting.
Get frequency map of words. <word, freq>

sort words, by freq, then by lexicography

loop through words to get unique words in answer.

Better plan:
- Lexicographical sorting heap
words = ["cake","ice","cake",,"ice","apple","juice","juice"] k = 3
output: ["cake", "ice", "juice"]

{
    "cake": 2,
    "ice": 2,
    "apple": 1,
    "juice": 2
}


freq-word{
    2: ["cake", "ice", "juice"],
    1: ["apple"]
}


top_3 values = [_, _, _]
sort values from largest to smallest

init ans
freq map top_3_values
move through freq map
get array mapping to freq-word map
get k_sub: count needed for ans

get k_sub smallest out of array
add to ans


Implement
"""

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = Counter(words) # O(n)
        # print(word_freq)

        top_k_freq_heap = [0] * k
        for freq in word_freq.values(): # n
            if freq > top_k_freq_heap[0]:
                heapreplace(top_k_freq_heap, freq) # log (k)
        # n log (k) ||||
        # print("top_k_freq_heap:", top_k_freq_heap)
        top_k_freq = deque() # k
        while top_k_freq_heap:
            top_k_freq.appendleft(heappop(top_k_freq_heap)) # log k

        # k log (k)
        # print("top_k_freq:", top_k_freq)
        top_k_freq = Counter(top_k_freq) # O(k)

        freq_word = defaultdict(list)
        for word, freq in word_freq.items(): # O(n)
            freq_word[freq].append(word) # O(1)
        # print(freq_word)
        
        ans = []
        BIG_CH = chr(ord('z') + 1)
        for freq, freq_count in top_k_freq.items():
            first_words_heap = [BIG_CH] * freq_count
            for word in freq_word[freq]:
                if word < first_words_heap[0]:
                    heapreplace_max(first_words_heap, word) # log(freq_count)

            first_words = deque()
            while first_words_heap:
                first_words.appendleft(heappop_max(first_words_heap))

            ans.extend(first_words)
        # ~~~~: kO(log max(freq_count))

        return ans

"""
Reviewed.

Evaluate.
n => len(words), worst case
Space: O(n) -> word -> freq, freq -> word. first_wrods, heaps

Time:
|||| -> O(n log (k))


"""