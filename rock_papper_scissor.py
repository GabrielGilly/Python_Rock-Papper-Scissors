# 1. welcome message and explaination of to play the first run
welcome_message=["Welcome to the rock papper scissor game."]
welcome_message.append('+---------------------------------+')
welcome_message.append("To play enter the letter of your choice:")
item=['Rock','Papper','Scissors','Rock']
welcome_message.append("0 = Rock")
welcome_message.append("1 = Papper")
welcome_message.append("2 = scissor")
welcome_message.append("+---------------------------------+")
welcome_message.append("You make the first move, what is your choice ?")

for i in welcome_message:
    print(i)

# 2. first run
player=int(input())
player_result=item[player]
print("You choose",player_result)

import random
computer=random.randint(0,2)
computer_result=item[computer]
print("The computer choose",computer_result)
print("+---------------------------------+")
#3. result
if item[player+1]==computer_result:
    victory=-1
elif player_result==computer_result:
    victory=0
elif item[computer+1]==player_result:
    victory=1

if victory==1:
    print("You won!")
elif victory==-1:
    print("You lost!")
elif victory==0:
    print("no victors")


#4. do you want to play again ?
#5. log result
#6. create statistics
#7. display statistics
#8. log the statistics in a game logger
