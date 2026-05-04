"""
implement a program that prompts the user for a str of text and then outputs that same text but with all vowels
(A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""

def main():
    print(shorten(input("Short: ")))

def shorten(word):
    for vowel in "aeiouAEIOU":
        word = word.replace(vowel, "")
    return word

if __name__ == "__main__":
    main()
