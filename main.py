import random
import socket




def proposeNewGame(client):
    client.send("Would you like to play a game? (y/n)\n".encode())
    userSelection = client.recv(2048).decode()
    if userSelection == "y" or userSelection ==  "Y" :
       runGame(client) 
    elif userSelection == "n" or userSelection ==  "N" :
        print("Bye")

def runGame(client):
    # I made the game configurable :
    min = 1
    max = 20
    guesses= 3
    # I made the game configurable ^
    guessesLeft= guesses
    pick = random.randint(1, 20)
    client.send("Hi, How should i call you?\n")
    username = client.recv(2048).decode()
    client.send("Well, "+username+", I am thinking about a number between "+str(min)+" and "+str(max)+".")
    while guessesLeft > 0 :
        client.send("Take a guess:\n")
        userGuess = int(client.recv(2048).decode())
        if userGuess == pick:
            client.send("Correct! Good Job! You guessed the number in only "+str(guesses - guessesLeft + 1)+" guesses!")
            proposeNewGame(client)
            return True
        else:
            if pick < userGuess:
                client.send("Your guess is too high")
            else:
                client.send("Your guess is too low")
            guessesLeft-=1
    client.send("Game Over!😨😨 You run out of guesses!")
    proposeNewGame(client)
    return False

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.bind(("", 8000))
tcpSocket.listen(1)
print("Waiting for a client...")
(client) = tcpSocket.accept()
runGame(client)