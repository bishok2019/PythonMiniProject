import random
user_wins = 0
computer_wins = 0
draw = 0
options = ["r", "p", "s"]
full_names = {"r": "Rock", "p": "Paper", "s": "Scissors"}
# random_num = random.randint(0, 2)
# print(random_num)
while True:
    user_input = input("""Type "r" for Rock / "p" for Paper / "s" for Scissor or Q to quit: """).lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_num = random.randint(0, 2)
    computer_pick = options[random_num]
    print("Computer picked", full_names[computer_pick] + ".")

    if user_input == "r" and computer_pick == "s":
         print("You chose rock, that was hard. You won!")
         user_wins += 1

    elif user_input == "p" and computer_pick == "r":
         print("Paper covers Rock. You won!")
         
         user_wins += 1
    elif user_input == "s" and computer_pick == "p":
         print("Scissors cuts Paper. You won !")
         
         user_wins += 1

    elif user_input == computer_pick :
         print("Draw!")
         draw += 1
    
    else:
         print("You lost!")
         computer_wins +=1

print("You:", user_wins)
print("Computer:", computer_wins)
print("Tie:", draw)
if computer_wins == user_wins:
     print("Hence draw")
elif computer_wins > user_wins:
     print("Computer wins!")
else:
     print("You wins!")