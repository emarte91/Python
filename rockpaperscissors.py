from random import randint

player = input("Rock, Paper or Scissors?").lower()
opponent = randint(0,2)

if opponent == 0:
    computer = "rock"
elif opponent == 1:
    computer = "paper"
else:
	computer = "scissors"

print(f"Your opponent chooses {computer}" )
if player == computer:
	print("It's a tie!")
elif player == "rock":
	if computer == "scissors":
		print("player wins!")
	else:
		print("computer wins!")
elif player == "paper":
	if computer == "rock":
		print("player wins!")
	else:
		print("computer wins!")
elif player == "scissors":
	if computer == "paper":
		print("player wins!")
	else:
		print("computer wins!")
else:
	print("Please enter a valid move! Typo")
