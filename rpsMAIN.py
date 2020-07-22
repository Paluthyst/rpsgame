from random import randint
t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0, 2)]
player = False
while player == False:

    player = input("Choose Rock, Paper or Scissors: ")

    if player == computer:
        print("You tied with the computer :/")
    elif player == "Rock".lower():
        if computer == "Paper":
            print("You loose", computer, "beats", player)
        else:
            print("YOU WIN :)", computer, "looses to", player)

    elif player == "Paper".lower():
        if computer == "Scissors":
            print("You loose", computer, "beats", player)
        else:
            print("YOU WIN :)", computer, "looses to", player)

    elif player == "Scissors".lower():
        if computer == "Rock":
            print("You loose", computer, "beats", player)
        else:
            print("YOU WIN :)", computer, "looses to", player)
    else:
        print("ah ah ah that's not an option friend")
    player = input("Would you like to play again? Yes or No: ")
    if player == "Yes":
        print("OK here we go!")
        computer = t[randint(0, 2)]
        player = False
    else:
        print("Ok see ya")
        player == True