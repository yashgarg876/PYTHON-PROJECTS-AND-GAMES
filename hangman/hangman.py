import random
from words import word_list


def get_word():
	word = random.choice(word_list)
	return word.upper()


def play(word):
	word_completion = "_" * len(word)
	guessed = False
	guessed_letters = []
	guessed_words = []
	tries = 5
	print("Lets play hangman")
	print(display_hangman(tries))
	print(word_completion)
	print("\n")
	while not guessed and tries > 0:
		guess = input("Please guess a letter or word: ").upper()
		if len(guess) == 1 and guess.isalpha():
			if guess in guessed_letters:
				print("You have already guessed the letter", guess)

			elif guess not in word:
				print(guess, "is not in thew word.")
				tries -= 1
				guessed_letters.append(guess)

			else:
				print("Good Job,", guess, "is in the word")
				guessed_letters.append(guess)
				word_as_list = list(word_completion)
				indices = [i for i, letter in enumerate(word) if letter == guess]
				for index in indices:
					word_as_list[index] = guess
				word_completion = "".join(word_as_list)
				if "_" not in word_completion:
					guessed = True

		elif len(guess) == len(word) and guess.isalpha():
			if guess in guessed_words:
				print("You have already guessed the word", guess)
			elif guess != word:
				print(guess, "is not the word.")
				tries -= 1
				guessed_words.append(guess)
			else:
				guessed = True
				word_completion = word
		else:
			print("Not a valid guess.")
		print(display_hangman(tries))
		print(word_completion)
		print("\n")

	if guessed:
		print("Congo, you have guessed it right")
	else:
		print("Sorry, you ran out of trials" + word + ". Maybe next time")


def display_hangman(tries):
	stages = ["""
				   ----------
				   |         |
				   |         O
				   |       \\|/
				   |         |
				   |        / \\

			   """,
			   """

				   ----------
				   |         |
				   |         O
				   |       \\|/
				   |         |
				   |        /
			   """,
			   """

				   ----------
				   |         |
				   |         O
				   |       \\|/
				   |         |
				   |
			   """,
			   """

				   ----------
				   |         |
				   |         O
				   |         |
				   |         |
				   |
			   """,
			   """

				   ----------
				   |         |
				   |         O
				   |
				   |
				   |
			   """,
			   """

				   ----------
				   |         |
				   |
				   |
				   |
				   |
				"""
     ]
	return stages [tries]


def main():
	  word = get_word()
	  play(word)
	  while  input("Play Again? (Y/N)").upper() == "Y":
		  word = get_word()
		  play(word)



if __name__ == "__main__":
	main()
