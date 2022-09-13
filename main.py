import random


def proposeNewGame():
    userSelection = input("Would you like to play a game? (y/n)\n")
    if userSelection == "y" or userSelection ==  "Y" :
       runGame() 
    elif userSelection == "n" or userSelection ==  "N" :
        print("Bye")

def runGame():
    # I made the game configurable :
    min = 1
    max = 20
    guesses= 3
    # I made the game configurable ^
    guessesLeft= guesses
    pick = random.randint(1, 20)
    username = input("Hi, How should i call you?\n")
    print("Well, "+username+", I am thinking about a number between "+str(min)+" and "+str(max)+".")
    while guessesLeft > 0 :
        userGuess = int(input("Take a guess:\n"))
        if userGuess == pick:
            print("Correct! Good Job! You guessed the number in only "+str(guesses - guessesLeft + 1)+" guesses!")
            proposeNewGame()
            return True
        else:
            if pick < userGuess:
                print("Your guess is too high")
            else:
                print("Your guess is too low")
            guessesLeft-=1
    print("Game Over!😨😨 You run out of guesses!")
    proposeNewGame()
    return False

runGame()