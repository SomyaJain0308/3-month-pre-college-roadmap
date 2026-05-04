
"""
In a file called game.py, implement a program that:

Prompts the user for a level, 𝑛. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and 𝑛, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
"""
import random
while True:
    n=int(input("Level: "))
    if n>0:
        break
    else:
        continue
p=random.randint(1, n)
while True:
    try:
        x=int(input("Guess: "))
        if x<=0:
            continue
        if x<p:
            print("Too small!")
            continue
        elif x==p:
            print("Just right!")
            break
        elif x>p:
            print("Too large!")
            continue
    except ValueError:
        pass

