import random

rand_number = random.randint(1,20)
guess = 42
list_of_guesses = []
while guess != rand_number:
    guess = int(input('Guess the number between 1 and 20! Type your guess.'))
    list_of_guesses.append(guess)

    if guess > rand_number:
        print('The guess is too high!')
    elif guess < rand_number:
        print('The guess is too low!')
    elif guess == rand_number:
        print('You got it!')
        break
print ("You guessed the following numbers: ", list_of_guesses)

    



    
