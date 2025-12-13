import random
import time
print ('---------------------------------------------------------')
print ('------------------- "THE GUESSING GAME"-------------------')
print ('---------------------------------------------------------')
print ('I will think of a number between 1 and 100 and you will have to guess it')
secret_number = random.randint(1,100)
correct = False
user_guess = 0
while user_guess != secret_number:
  time.sleep(0.7)
  user_guess = int(input('What is your guess? '))
  time.sleep(1)
  if user_guess > secret_number:
    print ('Too high!')
  elif user_guess < secret_number:
    print ('Too low!')
  else:
      print('You guessed right!')
      correct = True