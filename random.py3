import random 

print("Guess which number(1-100) the computer generated!")

guesstaken=0
rand=random.randint(1, 100)
guess=0

while (guesstaken < 10):
	guess=input("Make a guess: ")
	guess2=int(guess)

	guesstaken= guesstaken +1
	if (guess2 == rand):
		print("Bravo!!! You found it")
		break
	if ( guess2 > rand and guesstaken < 10):
		print("You guessed a higher number")
		
	if (guess2 < rand and guesstaken < 10):
		print("You guessed a smaller number")
		
if (guess2 == rand):
	print("You managed to find the random generated number", str(rand), "with", guesstaken, "efforts!")

if (guesstaken >= 10):
	print("Game over. You exceeded the maximum amount of efforts you had. (only 9 times are allowed)")
	
	
