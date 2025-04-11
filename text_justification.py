"""
Understand.
Last line of words - no extra spaces.
0 < Words length < maxWidth
words[i] can't contain spaces.

Match.
String.

Plan.
width = 0
result
loop through each `word` in words.
    add up width until more than maxWidth.
    add collection to result and keep moving.
add last words to result

Implement.
"""

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        width = 0
        result = [[]]
        for word in words:
            word_len = len(word) + 1
            width += word_len
            break_word = width - 1 - maxWidth
            if break_word <= 0:
                result[-1].append(word)
                if break_word: continue
            word_count = len(result[-1])
            sentence_length = width - bool(break_word)*word_len - word_count
            space_needed = maxWidth - sentence_length
            space_count = word_count - (word_count > 1)
            min_space = space_needed // space_count
            extra_space = space_needed - min_space*space_count
            word_count += word_count == 1  # so it will work for 1
            for i in range(word_count - 1):
                result[-1][i] += ' ' * (min_space + (extra_space > 0))
                extra_space -= 1
            result[-1] = "".join(result[-1])
            result.append([word] * bool(break_word))
            width = break_word and word_len
        if result[-1]:
            last_sentence = ' '.join(result[-1])
            result[-1] = last_sentence + ' ' * (maxWidth - len(last_sentence))
        else:  # Empty list from result.append([])
            result.pop()
        return result

"""
Review.
Last sentence. If sentence contains one word only.
What if last sentence is not a list? Is this possible?
Test case: ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"], 16
Last sentence was an empty list!

Evaluate.
n is len(words), k is max len(word)
Not counting result
Space: O(n * k) (Could be O(1) too, depending on how the inner forloop is analyzed)
Time: O(n * k) n, inner for loop in case of word_break time
"""