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
def play() -> set:
    # 2. first run
    print("You make the first move, what is your choice ?")
    item=['Rock','Papper','Scissors','Rock']
    player=int(input())
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

play()

#4. do you want to play again ?
i=1
while i ==1:
    print("Do you want to play again ?")
    print("Press ENTER key to play again or type no + press ENTER.")
    again=str(input())
    if again=='no':
        i=0
    else:
        play()
#5. log result
#6. create statistics
#7. display statistics
#8. log the statistics in a game logger
