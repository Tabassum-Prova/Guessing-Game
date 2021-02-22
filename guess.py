import random
true_number = random.randint(1, 49)
print(true_number)
guess_number = int(input("Enter your guess between 1 and 49: "))
print(guess_number)
while True:
    if guess_number == true_number:
        print("YOU ARE RIGHT! GOOD JOB!")
        break

    elif guess_number < true_number:
        print("YOUR GUESS IS LOW, TRY AGAIN")
        guess_number = int(input("Enter your guess between 1 and 49: "))

    elif guess_number > true_number:
        print("YOUR GUESS IS HIGH, TRY AGAIN")
        guess_number = int(input("Enter your guess between 1 and 49: "))