#prject 19 the rock, paper and scissers game
#method 1
# import random
# print ("Welcome to the Rock, Paper, Scissors game...")
# a = input ("Press Enter to contiune or type (Help) for the rules help:").lower()
# if a :
#     print ("""
#            ******** RULES ********
#            1) You chiise abd tge computer chooses
#            2) Rock smashes Scissors -> Roxk wins 
#            3) Scissors cut paper -> Scissors win 
#            4) Paper covers Rock -> Paper wins""")
# b = input ("Enter your choice  (rock, paper, scissors):").lower()
# group = ['rock', 'paper', 'scissors']
# c = random.choice(group)
# if a in group:
#     if b == 'rock' and c == 'paper':
#         d = "You lose, paper beats rock"
#     elif b == 'rock' and c == 'scissors':
#         d = "You win, rock beats scissors"
#     elif b == 'paper' and c == 'rock':
#         d = "You win, paper beats rock"
#     elif b == 'paper' and c == 'scissors':
#         d = "You lose, scissors beat paper"
#     elif b == 'scissors' and c == 'rock':
#         d = "You lose, rock beats scissors"
#     elif b == 'scissors' and c == 'paper':
#         d = "You win, scissors beat paper"
#     else:
#         d = "It's a tie!"
#     if b == 'rock':
#         print ("""your choice 
#         _______
#     ---'   ____)
#         (_____)
#         (_____)
#         (____)
#     ---.__(___)""")
#     elif b == 'paper':
#         print ("""your choice 
#         _______
#     ---'    ____)____
#             ______)
#             _______)
#             _______)
#     ---.__________""")
#     elif b == 'scissors':
#         print ("""your choice 
#         _______
#     ---'   ____)____
#             ______)
#         __________)
#         (____)
#     ---.__(___)""")
#     if c == 'rock':
#         print ("""computer choice
#         _______
#     ---'   ____)
#         (_____)
#         (_____)
#         (____)
#     ---.__(___)""")
#     elif c == 'paper':
#         print ("""computer choice 
#         _______
#     ---'    ____)____
#             ______)
#             _______)
#             _______)
#     ---.__________""")
#     elif c == 'scissors':
#         print ("""computer choice
#         _______
#     ---'   ____)____
#             ______)
#         __________)
#         (____)
#     ---.__(___)""")
#     print (d)
# else:
#     print ("invild entery")

#method 2
import random

print("Welcome to the Rock, Paper, Scissors game...")

a = input("Press Enter to continue or type (help) for the rules: ").lower()

if a == "help":
    print("""
    ******** RULES ********
    1) You choose, and the computer chooses.
    2) Rock smashes Scissors -> Rock wins.
    3) Scissors cut Paper -> Scissors win.
    4) Paper covers Rock -> Paper wins.
    """)

group = ["rock", "paper", "scissors"]

b = input("Enter your choice (rock, paper, scissors): ").lower()

if b not in group:
    print("Invalid entry. Please enter rock, paper, or scissors.")
else:
    c = random.choice(group)  # Computer's choice

    # Determine the winner
    if b == c:
        d = "It's a tie!"
    elif (
        (b == "rock" and c == "scissors") 
        or (b == "scissors" and c == "paper") 
        or (b == "paper" and c == "rock")):
        d = "You win!"
    else:
        d = "You lose!"

    # ASCII Art representations
    ascii_art = {
        "rock": """
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
        """,
        "paper": """
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
        """,
        "scissors": """
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
        """
    }

    print(f"Your choice:\n{ascii_art[b]}")
    print(f"Computer's choice:\n{ascii_art[c]}")
    print(d)