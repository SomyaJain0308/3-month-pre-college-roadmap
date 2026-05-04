
"""
In a file called professor.py, implement a program that:
Prompts the user for a level, 𝑛. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 𝑛 digits.
No need to support operations other than addition (+).
Note: The order in which you generate x and y matters. Your program should generate random numbers in x, y pairs to simulate generating one
math question at a time (e.g., x0 with y0, x1 with y1, and so on).
Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt
the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries,
the program should output the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 10.
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and
generate_integer returns a single randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:
"""

import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        X = generate_integer(level)
        Y = generate_integer(level)
        Z = X + Y
        for t in range(3):
            try:
                A = int(input(f"{X} + {Y} = "))
            except ValueError:
                print("EEE")
                if t == 2:
                    print(f"{X} + {Y} = {Z}")
                continue
            if A != Z:
                print("EEE")
                if t == 2:
                    print(f"{X} + {Y} = {Z}")
                continue
            else:
                score += 1
                break
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            l = int(input("Level: "))
            if l == 1 or l == 2 or l == 3:
                return l
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()

