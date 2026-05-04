import random
print("------------------------------------------------------------------------------------------------")
print("Welcome to the Lord's Casino!")
print("There are no losers, there are either winners or quitters.")
print("Question is which one are you?")
while True:
    ready=input("Are you ready? (Type Yes or No) ").lower()
    print("------------------------------------------------------------------------------------------------")
    if ready== "yes":
        break
    elif ready== "no":
        print("Fuck off then you dumb fuck!")
        print("Press 'Control+C' while inside Terminal if you want to exit else type Yes")
        continue
    else:
        print("Type yes or no Retard!")
        continue
# Explain the game
print("------------------------------------------------------------------------------------------------")
print("1) The game will ask you to place a bet.")
print("2) You will place a bet of amount between 1 and 100.")
print("3) There are 5 items which will spin randomly.")
print("4) If you manage to get all 5 items to be the same you get 100x the money you bet initally.")
print("5) If you manage to get 4 items to be the same you get 10x the money you bet initally.")
print("6) If you manage to get 3 items to be the same you get the money you bet initally.")
print("7) If you get less than 3 then I mean thanks for the money. Hope you lose again LOL")
print("------------------------------------------------------------------------------------------------")
while True:
    proceed=input("Do you wish to proceed? (Type Yes or No) ")
    print("------------------------------------------------------------------------------------------------")
    if proceed== "yes":
        break
    elif proceed== "no":
        print("Fuck off then you dumb fuck!")
        print("Press 'Control+C' while inside Terminal if you want to exit else type Yes")
        continue
    else:
        print("Type yes or no Retard!")
        continue
# Set inital Balance and Ask to make a bet not above the initial balance!
current_balance=100
while True:
    print("------------------------------------------------------------------------------------------------")
    print("This is your current balance:", current_balance)
    if current_balance<=0:
        print("You're broke, get out of my casino.")
        break
    while True:
        bet=int(input("How much will you bet? "))
        if 0<bet<=current_balance:
            break
        elif bet>current_balance:
            print("Retard you can't bet more than the current balance!")
            continue
        elif bet==0:
            print("Yo Retard you can't bet 0 money!")
            continue
        else:
            print("Yo retard you can't bet negative money!")
            continue
    symbols = ["🍒", "🍋", "⭐", "💎", "🍀"]
    results = [random.choice(symbols) for _ in symbols]
    print(" ".join(results))
    most_common = max(symbols, key=results.count)
    print(most_common, results.count(most_common))
    if results.count(most_common)<=2:
        print("Keep going till my wallet is full and your balance is zero!")
        current_balance=current_balance-bet
    elif results.count(most_common)==3:
        print("Congrats you just doubled your bet money!")
        current_balance=current_balance+(bet*1)
    elif results.count(most_common)==4:
        print("Congrats you just increased your balance by 10x your bet money!")
        current_balance=current_balance+(bet*10)
    else:
        print("Damn you just hit the JACKPOT!")
        current_balance+= (bet*1000)
    print("Current Balance:", current_balance)
    loop=input("Do you want to continue? (Type Yes or No) ").lower()
    if loop=="yes":
        continue
    elif loop=="no":
        print("Pussy!")
        break
    else:
        print("Should have typed yes or no we are continuing tho retard!")
        continue
