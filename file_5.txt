import random

# Generate random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0

print("🎯 Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("📉 Too low!")

        elif guess > secret_number:
            print("📈 Too high!")

        else:
            print("🎉 Correct! You guessed the number.")
            print("Total attempts:", attempts)
            break

    except ValueError:
        print("❌ Please enter a valid number!")