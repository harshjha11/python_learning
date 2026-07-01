"""
Self-Intro Script Generator

Features:
- Input validation
- Multiple introduction styles
- Colored terminal output
- Save intro as TXT
- Save user details as JSON
- Timestamp
- Repeat generation loop

Author: Harsh Jha
"""

import json
from datetime import datetime

from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)


BORDER = "*" * 80


def print_header():
    """Display the application header."""
    print(Fore.CYAN + BORDER)
    print(Fore.YELLOW + "        Welcome to the Self-Intro Script Generator")
    print(Fore.CYAN + BORDER)


def get_valid_age():
    """Validate age input."""
    while True:
        age = input("How old are you? ").strip()

        if age.isdigit() and 0 < int(age) <= 120:
            return int(age)

        print(Fore.RED + "Please enter a valid age.")


def choose_style():
    """Allow user to choose introduction style."""

    print("\nChoose Introduction Style")
    print("1. Formal")
    print("2. Friendly")
    print("3. Funny")

    while True:
        choice = input("Enter your choice (1-3): ").strip()

        if choice in ("1", "2", "3"):
            return choice

        print(Fore.RED + "Invalid choice. Please select 1, 2 or 3.")


def get_user_details():
    """Collect user information."""

    print()

    name = input("What is your name? ").strip().title()
    age = get_valid_age()
    city = input("Which city do you live in? ").strip().title()
    profession = input("What is your profession? ").strip().title()
    hobby = input("What is your favorite hobby? ").strip().title()

    style = choose_style()

    return {
        "name": name,
        "age": age,
        "city": city,
        "profession": profession,
        "hobby": hobby,
        "style": style,
    }


def generate_intro(user):
    """Generate introduction based on selected style."""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if user["style"] == "1":
        intro = (
            f"Good day! My name is {user['name']}. "
            f"I am {user['age']} years old and currently reside in {user['city']}. "
            f"I work as a {user['profession']}. "
            f"In my leisure time, I enjoy {user['hobby'].lower()}. "
            f"It is a pleasure to meet you."
        )

    elif user["style"] == "2":
        intro = (
            f"Hello! My name is {user['name']}. "
            f"I'm {user['age']} years old and live in {user['city']}. "
            f"I work as a {user['profession']} and absolutely enjoy "
            f"{user['hobby'].lower()} during my free time. "
            f"Nice to meet you!"
        )

    else:
        intro = (
            f"Hey there! I'm {user['name']} from {user['city']}. "
            f"I'm {user['age']} years young and somehow convinced people to let me work as a "
            f"{user['profession']}! "
            f"When I'm not doing that, you'll probably find me "
            f"{user['hobby'].lower()}. Life's too short to be boring!"
        )

    intro += f"\n\nLogged on: {timestamp}"

    return intro


def save_intro_txt(name, intro):
    """Save introduction to text file."""

    filename = f"{name.lower().replace(' ', '_')}_intro.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(intro)

    return filename


def save_user_json(user):
    """Save user information as JSON."""

    filename = f"{user['name'].lower().replace(' ', '_')}.json"

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(user, file, indent=4)

    return filename


def display_intro(intro):
    """Print formatted introduction."""

    print()
    print(Fore.GREEN + BORDER)
    print(Fore.WHITE + intro)
    print(Fore.GREEN + BORDER)


def main():
    """Main program."""

    print_header()

    while True:

        user = get_user_details()

        intro = generate_intro(user)

        display_intro(intro)

        txt_file = save_intro_txt(user["name"], intro)
        json_file = save_user_json(user)

        print(Fore.CYAN + f"\nIntroduction saved as: {txt_file}")
        print(Fore.CYAN + f"User data saved as: {json_file}")

        again = input(
            "\nGenerate another introduction? (y/n): "
        ).strip().lower()

        if again != "y":
            print(Fore.YELLOW + "\nThank you for using the generator!")
            break


if __name__ == "__main__":
    main()