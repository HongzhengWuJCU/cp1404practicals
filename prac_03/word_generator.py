"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random
import string
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

LETTER=string.ascii_lowercase
word_format = input("Input your word_format ((#, %, *, or letters): ").lower()
word=""
for kind in word_format:
    if kind == "#":
        word += random.choice(VOWELS)
    elif kind =="%":
        word += random.choice(CONSONANTS)
    elif kind =="*":
        word+= random.choice(LETTER)
    else:
        word+=kind
print(word)