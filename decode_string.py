"""
I made sure to pass through once.
When it's recursive, it will return on encountering ']'.
The recursive answer will be added to letters as if it were a character.

The return value for recursive calls is different from that for normal calls.
recursive will also return an index indicating the location that the calling code should
continue from.
"""

class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        def decode(start=0, recursive=False):
            num, result, letters, add_letter, i = 0, [], [], False, start
            while i < n:
                ch = s[i]
                if ch == '[':
                    add_letter = True
                    i += 1
                    continue

                if ch == ']':
                    compiled = "".join(letters)*num
                    if recursive:
                        return compiled, i+1
                    result.append(compiled)
                    add_letter, num, letters = False, 0, []
                    i += 1
                    continue

                if ch.isdigit():
                    if add_letter:
                        word, i = decode(i, recursive=True)
                        letters.append(word)
                        continue
                    num = num*10 + int(ch)
                else:
                    add_letter = True
                    letters.append(ch)

                i += 1

            result.append("".join(letters))
            return "".join(result)
        
        return decode()
