"""
UMPIRE
Understand
Case-insensitve
ASdlaF -> second row. .lower() should help.
words[i] i in {lowercase+uppercase}

Input: ["Daniel", "Dakaj", "Report", "Tower", "Prey", "Pointer"]
Ouput: ["Dakaj", "Report", "Tower", "Prey", "Pointer"]

Match:
Hashing. Sets.

Plan.
convert rows of keyboards to sets
keyboard_rows = [
    set("qwertyuiopQWERTYUIOP"),
    set("asdfghjklASDFGHJKL"),
    set("zxcvbnmZXCVBNM")
]
letter_to_row = {}
for i, keyboard_row in keyboard_rows:
    for ch in keyboard_row:
        letter_to_row[ch] = i

one_row_words = []

loop through words
for each word in words
    convert to lower case
    check first character of word to get row of keyboard
    keyboard_row = keyboard_rows[letter_to_row[word[0]]]
    for ch in word:
        if ch not in keyboard_row:
            break
    else:
        one_row_words.append(word)

return one_row_words


"""

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard_rows = [
            set("qwertyuiopQWERTYUIOP"),
            set("asdfghjklASDFGHJKL"),
            set("zxcvbnmZXCVBNM")
        ]

        letter_to_row = {}
        for i, keyboard_row in enumerate(keyboard_rows):
            for ch in keyboard_row:
                letter_to_row[ch] = i

        one_row_words = []

        for word in words:
            keyboard_row = keyboard_rows[letter_to_row[word[0]]]
            for ch in word:
                if ch not in keyboard_row:
                    break
            else:
                one_row_words.append(word)

        return one_row_words
