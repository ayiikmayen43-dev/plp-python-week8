"""
Python Multi-Tool Kit
----------------------
A interactive suite of everyday terminal utilities:
1. Number Guessing Game
2. Simple Calculator
3. To-Do List Manager
4. Countdown Timer
"""

import random
import time


# ==========================================
# TOOL 1: Number Guessing Game
# ==========================================
def number_guessing_game():
    """
    Generates a secret random number between 1 and 100, then prompts
    the user to guess until correct, offering higher/lower feedback.
    Uses: Loops, Conditionals, F-Strings, Random Module.
    """
    print("\n--- 🎯 Number Guessing Game ---")
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while not guessed:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("⚠️ Please enter a number within the range of 1 to 100.")
                continue

            if guess < secret_number:
                print("📈 Too low! Try guessing higher.")
            elif guess > secret_number:
                print("📉 Too high! Try guessing lower.")
            else:
                print(f"🎉 Congratulations! You guessed the secret number {secret_number} in {attempts} attempt(s)!")
                guessed = True
        except ValueError:
            print("⚠️ Invalid input. Please enter a valid whole number.")


# ==========================================
# TOOL 2: Simple Calculator
# ==========================================
def simple_calculator():
    """
    Performs basic arithmetic operations (+, -, *, /) on two user-provided numbers.
    Uses: Conditionals, User Input Casting, F-Strings.
    """
    print("\n--- 🧮 Simple Calculator ---")
    
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ").strip()
        num2 = float(input("Enter the second number: "))

        if operator == "+":
            result = num1 + num2
            print(f"✅ Result: {num1} + {num2} = {result}")
        elif operator == "-":
            result = num1 - num2
            print(f"✅ Result: {num1} - {num2} = {result}")
        elif operator == "*":
            result = num1 * num2
            print(f"✅ Result: {num1} * {num2} = {result}")
        elif operator == "/":
            if num2 == 0:
                print("⚠️ Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"✅ Result: {num1} / {num2} = {result:.2f}")
        else:
            print(f"⚠️ '{operator}' is not a valid operator. Please use +, -, *, or /.")
    except ValueError:
        print("⚠️ Invalid numerical input. Please enter valid numbers.")


# ==========================================
# TOOL 3: To-Do List Manager
# ==========================================
def todo_list_manager():
    """
    Allows users to view, add, and remove items from a dynamic to-do list.
    Uses: Lists (dynamic modification), Loops, Conditionals, F-Strings.
    """
    print("\n--- 📝 To-Do List Manager ---")
    todo_list = []

    while True:
        print("\nTo-Do List Sub-Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Return to Main Menu")
        
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            if not todo_list:
                print("📋 Your to-do list is currently empty!")
            else:
                print("\nYour Current Tasks:")
                for index, task in enumerate(todo_list, start=1):
                    print(f"  {index}. {task}")
        elif choice == "2":
            new_task = input("Enter the new task: ").strip()
            if new_task:
                todo_list.append(new_task)
                print(f"✅ Added: '{new_task}'")
            else:
                print("⚠️ Task description cannot be blank.")
        elif choice == "3":
            if not todo_list:
                print("⚠️ No tasks available to remove.")
            else:
                print("\nTasks:")
                for index, task in enumerate(todo_list, start=1):
                    print(f"  {index}. {task}")
                try:
                    task_num = int(input("Enter the number of the task to remove: "))
                    if 1 <= task_num <= len(todo_list):
                        removed_task = todo_list.pop(task_num - 1)
                        print(f"🗑️ Removed: '{removed_task}'")
                    else:
                        print("⚠️ Invalid task number.")
                except ValueError:
                    print("⚠️ Please enter a valid number.")
        elif choice == "4":
            print("Returning to Main Menu...")
            break
        else:
            print("⚠️ Invalid sub-menu choice. Please enter a number from 1 to 4.")


# ==========================================
# TOOL 4: Countdown Timer
# ==========================================
def countdown_timer():
    """
    Accepts a target number of seconds and counts down to zero displaying formatted time.
    Uses: Time Module, Loops, Formatting, F-Strings.
    """
    print("\n--- ⏳ Countdown Timer ---")
    try:
        seconds = int(input("Enter countdown time in seconds: "))
        if seconds <= 0:
            print("⚠️ Please enter a positive number of seconds.")
            return

        print(f"Starting countdown for {seconds} second(s)...")
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            timer_format = f"{mins:02d}:{secs:02d}"
            print(f" ⏱️  {timer_format}", end="\r")
            time.sleep(1)
            seconds -= 1

        print("\n🔔 Time's up!")
    except ValueError:
        print("⚠️ Invalid input. Please enter a valid whole number of seconds.")


# ==========================================
# MAIN PROGRAM LOOP
# ==========================================
def main():
    """
    Displays the welcoming message and maintains the core menu loop.
    Survives invalid choices and handles application termination cleanly.
    """
    print("==========================================")
    print("🌟 WELCOME TO THE PYTHON MULTI-TOOLKIT 🌟")
    print("==========================================")
    print("Your one-stop utility program for games and tools.")

    while True:
        print("\n==========================================")
        print("           PYTHON TOOLKIT MENU            ")
        print("==========================================")
        print("1. Number Guessing Game")
        print("2. Simple Calculator")
        print("3. To-Do List Manager")
        print("4. Countdown Timer")
        print("5. Quit")
        print("==========================================")

        user_choice = input("Enter your choice (1-5): ").strip()

        if user_choice == "1":
            number_guessing_game()
        elif user_choice == "2":
            simple_calculator()
        elif user_choice == "3":
            todo_list_manager()
        elif user_choice == "4":
            countdown_timer()
        elif user_choice == "5":
            print("\n👋 Thank you for using the Python Toolkit! Have a great day!")
            break
        else:
            print(f"\n⚠️ '{user_choice}' is not a valid option.")
            print("Please select a valid menu option from 1 to 5.")


if __name__ == "__main__":
    main()
