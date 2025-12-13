import random
import time
print ('---------------------------------------------------------')
print ('------------------- "THE GUESSING GAME"-------------------')
print ('---------------------------------------------------------')
print ('I will think of a number between 1 and 100.')
print ('You have to guess the correct number but you only have 7 attempts.')
secret_number = random.randint(1,100)
correct = False
user_guess = 0
max_attempts = 7
attempts = 0
while user_guess != secret_number:
  time.sleep(0.7)
  try:
    user_guess = int(input('What is your guess? '))
  except ValueError:
    print ('Please choose a number between 1 and 100')
    continue
  if user_guess < 1 or user_guess > 100:
    print ('Please choose a number between 1 and 100')
    continue
  attempts = attempts + 1
  time.sleep(1)
  if user_guess > secret_number:
    print ('Too high!')
  elif user_guess < secret_number:
    print ('Too low!')
  else:
      print('You guessed right!')
      correct = True
  print ('Attempts:', attempts)
  if attempts == max_attempts:
    print ('No attempts left. The secret number was ', secret_number)
    break
