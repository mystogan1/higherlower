from unicodedata import name
from art import vs as v, higherlower as hl
from gameData import data
import random
# Display .logo
print(hl)
# Generate a random account from gameData.
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

# Format the account data in printable format.
print(f"Choice A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
print(v)
print(f"Choice B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")

# Ask user to make a guess.

# Check if user is correct
# # Get follower count from gameData
# # Use if statement to check if user is correct

# Give user feedback on their guess.

# score keeping

# make game repeatable

# making an account at position B at A.