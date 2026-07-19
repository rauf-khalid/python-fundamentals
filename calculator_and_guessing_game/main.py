import random

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# Calculator  
def get_number(prompt):
    while True:
        raw_value = input(prompt).strip()
        try: 
            return float(raw_value)
        except ValueError:
            print(f"{raw_value} is not a valid number. Try again.")

OPERATIONS  = {
    "1": ("Add (+)", add),
    "2": ("Subtract (-)", subtract),
    "3": ("Multiply (x)", multiply),
    "4": ("Divide (/)", divide)
}

def run_calculator():
    print("\n--- Calculator ---")
    for key, (label, _) in OPERATIONS.items():
        print(f"{key}. {label}")
    choice = input("Choose an option: ").strip()

    if choice not in OPERATIONS:
        print("Invalid operation selected.")
        
    label, operation_func = OPERATIONS[choice]
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")

    try:
        result = operation_func(a, b)
        print(f"Result: {a} {label.split()[1]} {b} = {result}")
    except ZeroDivisionError as error:
        print(f"Error: {error}")

# Number Guessing Game
def get_valid_guess(low, high):
    while True:
        raw_value = input(f"Guess a number between {low} and {high}: ").strip()
        try:
           guess = int(raw_value)
        except ValueError:
            print("    Please enter a whole number.")
            continue

        if not ( low <= guess <= high):
            print(f"    Stay within {low}-{high}.")
            continue

        return guess

def play_round(low=1, high=100, max_attempts=10):
    secret_number = random.randint(low, high)
    attempts_used = 0

    while attempts_used < max_attempts:
        guess = get_valid_guess(low, high)
        attempts_used += 1

        if guess == secret_number:
            print(f"Correct! You got it in {attempts_used} attempt(s).")
            return
        if guess < secret_number:
            print("Too low.")
        if guess > secret_number:
            print("Too high.")
    
    print(f"Out of attempts. The number was {secret_number}")

def run_guessing_game():
    print("\n--- Number Guessing Game ---")
    while True:
        play_round()
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            return

# Main Menu
def main_menu():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Calculator\n2. Number Guessing Game\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            run_calculator()
        elif choice == '2':
            run_guessing_game()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again!")     



if __name__ == '__main__':
    main_menu()