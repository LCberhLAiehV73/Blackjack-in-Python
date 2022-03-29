# Made by Shell.json#6084
import random
import sys
import time

ComCard = 0
TotalComCard = 0
TotalCard = 0
card = 0

# Player choice
print("You have", TotalCard, "cards.")
print("""1)Hit
2)Stand""")
try:
    choice = str(input(""))
    if choice == '1' or 'hit' or 'h' or 'Hit':
        while True:
            card = random.randint(2, 10)
            print("You drew a", card)
            TotalCard = TotalCard + card
            print('You now have', TotalCard, "\n")
            if TotalCard > 21:
                print("Bust!")
                sys.exit()
            repeat = input("""1)Hit
2)Stand \n""")
            if repeat == '1':
                print("")
            if repeat == '2':
                break

    for i in range(5):
        ComCard = random.randint(2, 10)
        time.sleep(1)
        print('Alan drew a', ComCard)
        TotalComCard = ComCard + TotalComCard
        print('Alan now has', TotalComCard, 'cards\n')
        if TotalComCard > 21:
            print("Bust! You win!")
            time.sleep(3)
            sys.exit()
            # Win condition
        if TotalComCard > TotalCard:
            print("You lose!")
            time.sleep(1)
            sys.exit()
except TypeError:
    print("")
