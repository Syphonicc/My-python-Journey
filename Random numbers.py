import random
# low = 1
# high = 100
# options = ("rock", "paper", "scissors")
# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10","J","Q","K","A"]
# #number = random.randint(low,high)
# #random.random() = returns a floating point number from 0 to 1
# #number = random.random()
# #option = random.choice(options)
# random.shuffle(cards)
#
# print(options)


lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)
guesses = 0
is_running = True
print("Python number guessing game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess <  lowest_num or guess > highest_num:
            print("The number you have selected is out of range")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"Correct!")
            print(f"Number of guesses: {guesses}")
    else:
        print("write a valid number ")








