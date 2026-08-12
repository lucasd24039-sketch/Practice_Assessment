'''
    author: Lucas Donovan
    date: 12/08/2026
    version: 2
    description: Play a game of Heads or Tails against a robot.
'''
#----libraries----
import random 

#----functions----
def heads_tails(first_name):
    user_score = 0
    computer_score = 0
    options = ["Heads", "Tails"]

    while user_score != 2 and computer_score != 2:
        computer_guess = random.choice(options)
        user_guess = input("Heads or Tails: ")

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
print("Hi! Welcome to my Heads or Tails game.")
first_name = input("What is your name? ")
heads_tails(first_name)
