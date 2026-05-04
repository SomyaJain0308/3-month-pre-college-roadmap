"""
In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein X is a non-negative integer and Y is a positive integer,
and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the
tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any
exceptions like ValueError or ZeroDivisionError.
"""
while True:
    while True:
        try:
            fraction=input("Fraction: ")
            X, Y=fraction.split("/")
            if X.isnumeric() and Y.isnumeric() and int(Y)>=int(X) and int(Y)!=0:
                break
            else:
                continue
        except ValueError:
            pass
    X=int(X)
    Y=int(Y)
    if X<0 or Y<=0:
        continue
    else:
        fraction=(X*100/Y)
        fraction=round(fraction, 0)
        fraction=int(fraction)
        if fraction<=1:
            print("E")
            break
        elif fraction>=99:
            print("F")
            break
        else:
            print(f"{fraction}%")
            break
