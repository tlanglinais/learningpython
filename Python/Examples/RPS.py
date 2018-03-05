#P2 Now random
from random import *

print("Welcome to the game!")
print("Enter rock, paper or scissors")
p1choice = input("Enter Player 1's Choice: ").lower()
choices = ['rock', 'paper', 'scissors']
p2choice = choices[randint(0,2)]
print(p2choice)
print('SHOOT')

#Check for a tie
if p1choice == p2choice:
	print("Tied")

#P1 chooses rock
elif p1choice == 'rock':

	#P2 chooses rock
	if p2choice == 'rock':
		print("Tied")

	#P2 chooses paper
	elif p2choice == 'paper':
		print("Player 2 Wins!")


#P1 chooses paper
elif p1choice == 'paper':

	#P2 chooses rock
	if p2choice == 'rock':
		print("Player 1 Wins!")

	#P2 chooses paper
	elif p2choice == 'paper':
		print("Tied")

#P1 chooses scissors
else:

	#P2 chooses rock
	if p2choice == 'rock':
		print("Player 2 Wins!")

	#P2 chooses paper
	elif p2choice == 'paper':
		print("Player 1 Wins!")