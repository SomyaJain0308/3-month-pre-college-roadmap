"""
In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s
format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the
library’s grid format. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv,
or if the specified file does not exist, the program should instead exit via sys.exit.
"""
import sys
from tabulate import tabulate
import csv
menu=[]
if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
if len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
with open(sys.argv[1]) as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        menu.append(row)
print(tabulate(menu, headers=header, tablefmt="grid"))
