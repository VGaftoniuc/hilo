import random

print("Welcome to the HiLo Game")

random_number = random.randint(0, 100)

while True:
    num = int(input("Please chose a number from 0 to 100: "))
    if num > random_number:
        print("Too high.")
    elif num < random_number:
        print("Too low.")
    else:
        print(f"That's right you guessed it. The answer is {num} !!!")
        break
