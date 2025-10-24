import random

secret = random.randint(1, 10)
guess = int(input("guess the number in between 1 to 10 "))

if guess == secret:
    print("Right" 🎯")
else:
    print(f"Nope the number was!{secret} 😅")