import random
random = random.randint(0,100)

guess = int(input("Enter guess between 0 - 100  "))

while(1):
    if guess < random:
        print("Guess Higher")
        guess = int(input("Enter guess between 0 - 100"))
    elif guess > random:
        print("Guess Lower")
        guess = int(input("Enter guess between 0 - 100"))
    else:
        print("Perfect guess")
        break