from re import A
from art import vs as v, higherlower as hl
from gameData import data
import random
from replit import clear



# Format the account data in printable format.
def format_data(account):
    '''Format the account data into printable format.'''
    acc_name = account["name"]
    acc_desc = account["description"]
    acc_country = account["country"]
    return f"{acc_name}, a {acc_desc}, from {acc_country}."

# Check if user is correct
def check_ans(guess,a_follower,b_follower):
    '''Take guess and return if its correct. '''
    if a_follower>b_follower:
        return guess == "a"
    elif a_follower<b_follower:
        return guess == "b"

account_b = random.choice(data)
score = 0
isGame = True

# make game repeatable
while isGame:
    # Display .logo
    print(hl)

    # Generate a random account from gameData.
    # # making an account at position B at A.
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(format_data(account_a))
    print(v)
    print(format_data(account_b))

    # Ask user to make a guess.
    guess = input("Make your guess: ").lower()

    # # Get follower count from gameData
    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]

    is_correct = check_ans(guess,a_follower,b_follower)

    clear()
    # Give user feedback on their guess.
    # # score keeping
    
    if is_correct:
        score+=1
        print(f"Right answer your score is {score}")
    elif not is_correct:
        print("Wrong answer.")
        isGame = False
    else:
        print("Enter 'a' or 'b'")


