"""
In a file called figlet.py, implement a program that:
Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name
of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font,
the program should exit via sys.exit with an error message.
"""
import sys
from pyfiglet import Figlet
figlet = Figlet()
figlet.getFonts()
if len(sys.argv)==3:
    while True:
        arg1=sys.argv[1]
        arg2=sys.argv[2]
        while True:
            if arg1=="-f":
                break
            elif arg1=="--font":
                break
            else:
                sys.exit(1)
        figlet.setFont(font=arg2)
        hi=input("Input: ")
        print(f"Output:, {figlet.renderText(hi)}")
        break
elif len(sys.argv)==1:
        hi=input("Input: ")
        print(f"Output:, {figlet.renderText(hi)}")
elif len(sys.argv)==2:
    sys.exit(1)
else:
     sys.exit(1)
