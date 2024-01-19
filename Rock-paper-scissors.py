import random

user_score = 0
comp_score = 0
    
for i in range(0,6):
    user = input()
    options = ["Rock","Paper","Scissors"]

    comp = random.choice(options)

    if user == comp:
        print("Tie!!!")
    elif user == "Paper" and comp == "Rock":
        print("Paper covers rock")
        user_score += 1
    elif user == "Scissors" and comp == "Paper":
        print("Scissors cuts paper")
        user_score += 1
    elif user == "Rock" and comp == "Scissors":
        print("Rock beats Scissors")
        user_score += 1
    else:
        print("Computer wins")
        comp_score += 1

 
 
if comp_score > user_score:
        print("Computer wins!! Score:", comp_score)
elif user_score > comp_score:
    print("User wins!! Score:", user_score)
else:
    print("It's a tie!!!, Score:", user_score)