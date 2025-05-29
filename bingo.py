import random

# Predefined Bingo dictionary (keys - numbers, values - False initially)
bingo = {i: False for i in range(1, 101)}

# Number of marked numbers required to win
winning_number = 10

marked_numbers_count = 0
game_continues = True

print("Game started!")

while game_continues:
    random_number = random.randint(1, 100)

    print(f"Drawn number: {random_number}")

    if bingo[random_number] == False: #Check if the number is not marked yet
        print(f"Marking number: {random_number}")
        bingo[random_number] = True # Mark the number
        marked_numbers_count += 1

        if marked_numbers_count == winning_number:
            print("Bingo! You won!")
            game_continues = False
    else:
        print(f"Number {random_number} was already marked.")

print("Bingo dictionary state after the game:", bingo) # For debugging
