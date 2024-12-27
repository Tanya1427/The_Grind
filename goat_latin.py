"""
People: Daniel Enesi. Eniola Akinpelumi.:)_Felix_name_
UMPIRE

Understand.
Vowel: aeiou => ma to end: apple -> applema
!(aeiou) => remove first letter and add to end, add ma.
            goat -> oatgma

Match:
String.

Plan.
Follow the rules.

vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

Easy way.
words = sentence.split(' ')
result = []

loop through
for i, word in enumerate(words):
    i => index
    word => value

    if word[0] in vowel:
        new_word = word + "ma"
    

    new_word += 'a' * (i+1)

return ' '.join(result)

Plan
"I speak Goat Latin"
result = ['I', "ma", 'a', ' ', 'p', 'e', 'a', 'k', 's', 'ma', 'aa', ' ']
return "".join(result)

....['I', "speak", "Goat", "Latin"]

["Imaa", "peaksmaa", "oatGmaaaa", "atinLmaaaaa"]
 => "Imaa peaksmaa oatGmaaaa atinLmaaaaa"

"I speak Goat Latin"
goat_latin = []
first_letter = ""

loop through ch
    if first_letter == "":
        first_letter = ch
        if first_letter is not vowel:
            continue
    if ch == ' ':
        if first_letter is not vowel:
            add to goat_latin
        add 'ma' to goat_latin
        add 'a'*(i+1) to goat_latin
        add ' '
        continue
    add ch to goat_latin


"""
class Solution:
    def toGoatLatin1(self, sentence: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        return ' '.join(
            (word if word[0] in vowels else word[1:] + word[0]) + "ma" + ('a' * (i+1)) for i, word in enumerate(sentence.split(' '))
        )

    def toGoatLatin(self, sentence: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        goat_latin = StringIO()
        first_letter = ""
        freq_a = 1

        for ch in sentence:
            if first_letter == "":
                first_letter = ch
                if first_letter not in vowels:
                    continue

            if ch == ' ':
                if first_letter not in vowels:
                    goat_latin.write(first_letter)

                goat_latin.write("ma" + 'a'*freq_a)
                first_letter = ""
                freq_a += 1

            goat_latin.write(ch)

        if first_letter not in vowels:
            goat_latin.write(first_letter)
        goat_latin.write("ma" + 'a'*freq_a)

        return goat_latin.getvalue()
