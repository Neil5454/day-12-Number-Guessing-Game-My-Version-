from random import randint

min_num = 1
max_num = 100
answer = randint(min_num, max_num)
print(answer)
print("Welcome to Number Guessing Game!")
# print(logo)
difficulty = input("Choose a difficulty. Type 'e' for easy or 'h' for hard. ")
if difficulty == "e":
  attempts = 10
else:
  attempts = 5

attempts_counter = 0
while attempts_counter < attempts:
  print(f"Your have {attempts - attempts_counter} attempts remaining to guess the number.")
  guess = int(input("Make a guess. "))
  if guess == answer:
    print("Your guessed the right number.")
    break
  elif guess > answer:
      print("Too high.  Guess Again.")
      attempts_counter += 1
  else:
      print("Too low.  Guess again.")
      attempts_counter += 1
else:
    print("You have no more attempts.")