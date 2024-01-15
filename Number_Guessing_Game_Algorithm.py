import random
number = random.randint(1, 100)


def chances(chance, luck):
    if luck < number:
        print("Too low")
        return chance - 1
    elif luck > number:
        print("Too high")
        return chance - 1
    else:
        print(f"You guessed correctly!\nThe answer is {luck}")
        return 'win'


def game(attempt):
    print("I am thinking of a number between 1 and 100.")
    print(f"You have {attempt} attempts to guess the number.\n")
    continuity = True
    while continuity:
        guess = int(input("Make a guess: "))
        attempt = chances(attempt, guess)
        if attempt == 'win':
            print("You win")
            continuity = False
        elif attempt > 0:
            print(f"You have {attempt} attempt(s) to guess the number.\n")
        elif attempt == 0:
            continuity = False
            print("You did not guess the number correctly and you have exhausted your attempts."
                  "\nYou lose.\nGame Over.\n")


def game_level(l):
    # attempts = 0
    if l == 'easy':
        attempts = 10
        game(attempts)
    elif l == 'hard':
        attempts = 5
        game(attempts)
    else:
        print("You did not select a defined option.")


print("Welcome to the number guessing game!!!")

replayer = True
while replayer:
    replay = input("Would you like to play the game?\nType 'y' or 'n': ")
    if replay == 'y':
        level = input("There are two levels: 'easy' or 'hard'\nEnter level: ").lower()
        game_level(level)
    elif replay == 'n':
        replayer = False
        print("GoodBye!!!")
    else:
        replayer = False
        print("You did not select a valid input.")
