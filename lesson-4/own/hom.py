from random import random


def uncommon_elements(x,y):
    newlist=[]
    for i in x:
        if i not in y:
            newlist.append(i)
    for i in y:
        if i not in x:
            newlist.append(i)
    return newlist
def square(n):
    for i in range(n):
        print(i*i)
def modify_string(txt):
    result=[]
    vowels='aeiou'
    for i, char in enumerate(txt):
        result.append(char)
        if (i+1)%3==0 or (char in vowels and i+1<len(txt)):
            result.append('_')
    return ''.join(result)
def numberguessinggame():
    while True:
        number=random.randint(1,100)
        attempts=10
        while attempts>0:
            guess=input(int("Make a guess: "))
            if guess > number:
                print("Too high")
            elif guess < number:
                print("Too low")
            else:
                print("Good job")
            attempts-=1
        choice = input("Do you want to continue? (Y/YES/y/yes/ok): ")
        if choice.lower() not in ['y', 'yes', 'ok']:
            break
def password_checker():
    password = input("Enter your password: ")
    if len(password) < 8:
        print("Your password must be at least 8 characters long")
    elif not any(char.isupper() for char in password):
        print("password should contain upper case letters")
    else:
        print(f"{password} is strong password")
def prime():
    isprime= True
    for i in range(1,100):
        for x in range(1,(i**0.5)+1):
            if i%x==0:
                isprime=False
                break
        if isprime:
            print(i)
def rps():
    choices=["rock","scissors","paper"]
    user,computer=0,0
    while user<5 and computer<5:
        user_choice=input("Input rock, paper, or scissors: ").lower()
        computer_choice=random.choice(choices)
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice=="rock" and computer_choice=="scissors") or \
            (user_choice=="scissors" and computer_choice=="paper") or \
            (user_choice=="paper" and computer_choice=="rock"):
            print("You win this round!")
            user+=1
        else:
            print("computer won this round")
            computer+=1
    if user==5:
        print("You win")
    else:
        print("You lose")






