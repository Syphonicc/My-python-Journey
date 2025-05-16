#Python Banking Program
# This program will focus on , Withdraw, Deposit ,Show Balance
Show_balance = 1
Deposit = 2
Withdraw = 3
total = 0
is_running = True
print("-------WELCOME TO THE PYTHON BANK-------")


while is_running:

    print("What would you like to do?(4 to quit)")
    options = ["Show balance : 1", "Deposit : 2", "Withdraw : 3"]

    for option in options:
        print(option)
    user_input = int(input("---------------------------->"))

    if user_input == 1:
        print(f"Your balance is {total}")


    elif user_input == 2:
        dep = int(input("How much would you like to deposit?"))
        total += dep
        print(f"You have succesfully deposited ${dep} amount")

    elif user_input == 3:
        wit = int(input("How much would you like to withdraw?"))
        total -= wit
        print(f"You have succesfully withdrawn ${wit} amount")

    elif user_input == 4:
            is_running =False
    else:
        print("The number is not valid")
