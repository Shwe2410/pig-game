import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll

while True:
    players = input("Enter the  number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("enter a number from 2-4")
    else:
        print("Enter a valid number")

max_score = 50
players_score = [0 for _ in range(players)]
#find the maximum score from players - max(players_score)
#check whether the players max score < max_score
while max(players_score) < max_score :
    for i in range(players):
        print("Player number ", i + 1, "has started!")
        current_score = 0
    
        while True:
            should_roll = input("do you wanna roll? (y)")
            #should change the case - should_roll = should_roll.lower()
            #if should_roll != "y"
            should_roll = should_roll.lower()
            if should_roll != "y":
                break
            dice_num = roll()
            # 
            if dice_num == 1 :
                current_score = 0
                print("your turn is over. You got 1")
                break
            else :
                print('you got ', dice_num)
                current_score += dice_num

            print("Your score is " , current_score) 
        
        players_score[i] = players_score[i]+current_score
        print("Your total score is ",players_score[i])
    print('Continue in the next round')

max_score = max(players_score)
winning_index = players_score.index(max_score)      
print("The player number ", winning_index + 1, "is the winner with a score of ",max_score)








