"""
implement a program that prompts the user for a str of text and then outputs that same text but with all vowels
(A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""
x=input("Short: ")
for vowel in "aeiouAEIOU":
    x=x.replace(vowel, "")

print(x)

