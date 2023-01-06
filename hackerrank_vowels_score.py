n = int(input())
words = []
for i in range(n):
    words.append(input())


def isVowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']


score = 0
for word in words:
    num_vowels = 0
    for letter in word:
        if isVowel(letter):
            num_vowels = num_vowels + 1

    if num_vowels % 2 == 0:
        score = score + 2
    else:
        score = score + 1
print(score)
