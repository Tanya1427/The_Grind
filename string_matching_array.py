
"""
Understand.
O(n-squared) will actually work. Lowercase. unique words.
Any order will allow sorting words. ANOTHER WORD.
Ignore the max_len, try to go as optimal as possible

Match.
KMP.

Plan

PMT for KMP...
A A A C A A A A
0 1 2 0 1 2 3 1

0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23
A  B  A  B  D  A  B  A  C  D  A   B   A   B   C   A   B   A   B   A   B   C   A   B

0  1  2  3  4  5  6
A  B  A  B  C  A  B

0  0  1  2  0  1  2
End PMT for KMP practice.

Sort words by len.
['as', 'mass', 'hero', 'superhero']

In one pass, get the first occurence of each len of string.
[0, 1, 3] Should avoid checking if len is same...
Also save the length. {2: 0, 4: 1, 9: 3}

Make the Partial Match Table of strs up to that of len less than longest
    Save the length of the longest Proper Prefix
    - that is also a Suffix of the string up to that position.

    Algorithm (def make_prefix_table(pattern)): initialize array lps (longest prefix suffix) having length of pattern.
    array start = 0, var len = 0, start from 1 at pattern.
    Move through pattern from index 1,
    if pattern[index] = pattern[len],
        save len in lps[index]
    else: set len to 0 again.
    A  B  A  B  C  A  B
    0  0  1  2  0  1  2

Answer MUST be among those of non-max length.
prefix_tables: [[0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
result = []
set saved_len = 0
saved_text_index = deque.popleft() or just deque.popleft()
while loop through prefix_tables with table_index:
    loop value: prefix_table
    string it corresponds to: pattern
    if saved_len != len(prefix_table):  # Reached higher text
        saved_len = len(prefix_table)
        set saved_text_index to deque.popleft()
    text_index = saved_text_index
    while text_index still cool:
        get words[text_index] as text
        if kmp(text, pattern, prefix_table):
            result.append(pattern)
            break
        text_index += 1
return result


"""
class Solution:
    def make_prefix_table(self, pattern):
        n = len(pattern)
        prefix_table = [0] * n
        prefix_length = 0
        i = 1
        while i < n:
            if pattern[prefix_length] == pattern[i]:
                prefix_length += 1
                prefix_table[i] = prefix_length
                i += 1
                continue
            if prefix_length != 0:
                prefix_length = prefix_table[prefix_length - 1]
                continue
            prefix_table[i] = prefix_length
            i += 1

        return prefix_table

    def kmp(self, text, pattern, prefix_table):
        pattern_indx = text_indx = 0
        n = len(pattern)
        m = len(text)
        while text_indx < m:
            if pattern[pattern_indx] == text[text_indx]:
                pattern_indx += 1
                text_indx += 1
                if pattern_indx == n:
                    return True
                continue
            if pattern_indx == 0:
                text_indx += 1
                continue
            pattern_indx = prefix_table[pattern_indx - 1]

        return False

    def stringMatching(self, words: List[str]) -> List[str]:
        # First sort by length... will help
        words.sort(key=len)
        # First occurence of each len of string
        lens_firsts = deque()
        cur_length = 0
        for i, length in enumerate(map(len, words)):
            if cur_length != length:
                cur_length = length
                lens_firsts.append(i)

        max_len = len(words[-1])
        prefix_tables = []
        for pattern in words:
            if len(pattern) == max_len:
                break
            prefix_tables.append(self.make_prefix_table(pattern))

        result = []
        saved_len = 0
        lens_firsts.popleft()  # Remove smallest's length
        prefix_tables_len = len(prefix_tables)
        words_len = len(words)
        for table_index, prefix_table in enumerate(prefix_tables):
            pattern = words[table_index]
            if saved_len != len(prefix_table):
                saved_len = len(prefix_table)
                saved_text_index = lens_firsts.popleft()
            text_index = saved_text_index
            while text_index < words_len:
                text = words[text_index]
                if self.kmp(text, pattern, prefix_table):
                    result.append(pattern)
                    break
                text_index += 1
        return result

"""
Review.

Evaluate:
n = len(words)
m = len(largest_word_in_words)
                    sort    fastindex   converting patterns    kmp pairing
Time: Worst Case: O(nlogn) + O(n) +     O(m*n)               +  O(m*n)
=> O(nlogn) + O(m*n) (hope I'm right)

Best case: there'll be many repeated lengths of words, so it'll skip.
Best case: there'll be many max_len words

Space: O(n)
"""
