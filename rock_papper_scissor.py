#modules
import pprint
import time
# function play
def play() -> set:
    # 2. first run
    run={} # dictionnarie for logger
    print("You make the first move, what is your choice ?")
    item=['Rock','Papper','Scissors','Rock']
    correct=0
    good=[0,1,2]
    while correct==0:
        entry_value=input()
        try:
            player=int(entry_value)
            if player in good:
                correct=1
            else:
                correct=0
                print("YOU NEED TO ENTER 0=Rock, 1=Papper, 2=Scissors")
        except ValueError:
            correct=0
            print("YOU NEED TO ENTER 0=Rock, 1=Papper, 2=Scissors")



    player_result=item[player]
    print("You choose",player_result,'.')
    import random
    computer=random.randint(0,2)
    computer_result=item[computer]
    print("The computer choose",computer_result,'.')
    print(line)
    #3. result
    if item[player+1]==computer_result:
            victory='computer'
            message='You lost !'
    elif player_result==computer_result:
            victory='stand'
            message='Nobody won.'
    elif item[computer+1]==player_result:
            victory='player'
            message='You won!'
    print()
    print('        ',message)
    print()
    print(line)
    ts=time.time()
    run={'datestamp':ts,'player':player_result,'computer':computer_result,'victory':victory}
    list_result.append(run)
# list for log
list_result=[]
# 1. welcome message and explaination of to play the first run
welcome_message="Welcome to the rock papper scissor game."
rules=["To play enter the number of your choice:"]
rules.append("0 = Rock")
rules.append("1 = Papper")
rules.append("2 = scissor")
line="+---------------------------------+"
print(line)
print(welcome_message)
for i in rules:
    print(i)
print(line)

# 2 first play
play()

# 3 result
"""within the function play"""

#4. do you want to play again ?
i=1
while i ==1:
    print("Do you want to play again ?")
    print("Press any key to play again, no to quit, stats to see the game statistics")
    again=str(input())
    if again=='no':
        i=0
    elif again=='stats':
        pprint.pprint(list_result)
    else:
        play()

#5. log result
"""to log result will create a list of dictionnaries with each dictionnraries containings:
- timestamp
- player_result
- computer_result
- victory
the log will then be written in a text file named game.log
"""

#6. create statistics
"""use the log to define
% victory player + total
% victory computer + total
% stand + total
number of match played"""
player_victory=0
computer_victory=0
stand=0
player_per=0
computer_per=0
stand_per=0

for i in list_result:
    print(i)
#7. display statistics
#8. log the statistics in a game logger
