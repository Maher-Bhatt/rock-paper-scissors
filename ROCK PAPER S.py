import random

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

game_images = [rock, paper, scissors]

print("HI WELCOME TO THE GAME OF ROCK PAPER SCISSORS")
print("HERE 0 IS FOR ROCK, 1 FOR PAPER, AND 2 FOR SCISSORS")

user_input = int(input("CHOOSE YOUR HAND: "))
if user_input >= 0 and user_input <= 2:
     print("You chose:")
     print(game_images[user_input])

     computer_choice = random.randint(0, 2)
     print("Computer chose:")
     print(game_images[computer_choice])

     if user_input == computer_choice:
      print("ITS A DRAW TRY AGAIN")
     elif (user_input==0 and computer_choice==2) or \
          (user_input==1 and computer_choice==0) or \
          (user_input==2 and computer_choice==1):
      print("YOU WIN")
     else: 
      print("YOU LOSE")
else:
  print("plz choose from 0,1,2")