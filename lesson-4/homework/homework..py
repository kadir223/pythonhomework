from collections import Counter
import random

def uncommon_elements(list1, list2):
    count1 = Counter(list1)
    count2 = Counter(list2)
    result = []
    for key in (count1.keys() | count2.keys()):
        if count1[key] != count2[key]:
            result.extend([key] * abs(count1[key] - count2[key]))
    return result

def print_squares(n):
    for i in range(1, n):
        print(i ** 2)

def modify_string(txt):
    result = []
    vowels = "aeiouAEIOU"
    for i, char in enumerate(txt):
        result.append(char)
        if (i + 1) % 3 == 0 or (char in vowels and i + 1 < len(txt)):
            result.append("_")
    return "".join(result)

def number_guessing_game():
    while True:
        number = random.randint(1, 100)
        attempts = 10
        while attempts > 0:
            guess = int(input("Enter your guess: "))
            if guess > number:
                print("Too high!")
            elif guess < number:
                print("Too low!")
            else:
                print("You guessed it right!")
                return
            attempts -= 1
        choice = input("You lost. Want to play again? (Y/YES/y/yes/ok): ")
        if choice.lower() not in ['y', 'yes', 'ok']:
            break

def password_checker():
    password = input("Enter your password: ")
    if len(password) < 8:
        print("Password is too short.")
    elif not any(char.isupper() for char in password):
        print("Password must contain an uppercase letter.")
    else:
        print("Password is strong.")

def print_primes():
    for num in range(2, 101):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    user_score, computer_score = 0, 0
    while user_score < 5 and computer_score < 5:
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
    if user_score == 5:
        print("You win the game!")
    else:
        print("Computer wins the game!")
