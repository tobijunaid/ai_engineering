import random
import time
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list_choice = [rock, paper, scissors]
player_choice = int(input("What do you choose? "
                      "Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if player_choice >= 0 and player_choice <= 2:
    print("You chose")
    print(list_choice[player_choice])
    
#Alternatively
# if player_choice == 0:
#     print(rock)
# elif player_choice == 1:
#     print(paper)
# elif player_choice == 2:
#     print(scissors)

computer_choice = random.randint(0,2)
print("Computer chose:")
print(list_choice[computer_choice])

if player_choice <0 or player_choice >= 3:
    print("You Entered a wrong Choice. You lose")
elif player_choice == computer_choice:
    print("It's a draw")
elif computer_choice == 0 and player_choice == 2:
    print("You lose")
elif computer_choice == 2 and player_choice == 0:
    print("You win")
elif computer_choice > player_choice:
    print("You lose")
elif computer_choice < player_choice:
    print("You win")

time.sleep(7)
print("Bye")
time.sleep(3)



