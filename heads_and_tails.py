'''
    author: Lucas Donovan
    date: 12/08/2026
    version: 2
    description: Play a game of Heads or Tails against a robot.
'''
#----libraries----
import random # used to let the computer randomly choose Heads or Tails
#----functions----
def force_name():
# makes an infinite loop, ensuring name is between 2 and 12 letters
    while(True):
# ensures users name is only letters
        name = input("Please type name: ")
        if len(name) >= 2 and len(name) <= 12 and name.isalpha():
            print("Name accepted:", name)
            # returns name back to variable that called the function
            return name
# prints error if name contains numbers / special characters
        else:
            print("ERROR -- please enter valid name")

def heads_tails(first_name):
     # initialise scores for both players
    user_score = 0
    computer_score = 0
    # possible options for the game
    options = ["Heads", "Tails", "heads", "tails"]

    # loop continues until someone reaches 2 points (best of 3)
    while user_score != 2 and computer_score != 2:
        computer_guess = random.choice(options) # computer randomly picks Heads/Tails
        user_guess = input("Heads or Tails: ") # user enters their guess

        # check if the user guessed correctly
        if user_guess == computer_guess:
            print("It was {}, you guessed {}, you won that round".format(computer_guess, user_guess))
            user_score += 1
        else:
            print("It was {}, you guessed {}, you lost that round".format(computer_guess, user_guess))
            computer_score += 1

    # best of 3 result
    if user_score == 2:
        print("{}, you won the game!".format(first_name))
    else:
        print("{}, you lost the game!".format(first_name))


#----main program----
print("Hi! Welcome to my Heads or Tails game.") # intro message
first_name=force_name()
heads_tails(first_name) # start the game
