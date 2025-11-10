import art
import random
from game_data import data #easier to use only variable, otherwise have to write game_data.data
print(art.logo)

#Compare the followers of both against each other
def compare(no_followers_a, no_followers_b, user_input, scoring_point): #parameters
    group_select= ""
    if no_followers_a> no_followers_b:
        group_select+="A"
    elif no_followers_a< no_followers_b:
        group_select+="B"

    if user_input==group_select:
        print(f"You are right. Your current score is {scoring_point+1}")
        return scoring_point+ 1 #keeping adding one digit up, whenever it equates with group_select
    else:
        return -1 

Score =0

Group_A = random.randint(0, 49)  
Group_B = random.randint(0, 49)
while Score!=-1: #while the Score is not -1, do the following Code, ie. while user_input!= group_select

    Group_A_pick = data[Group_A]  # data[index]
    print(f"Compare A: {Group_A_pick["name"]}, {Group_A_pick["description"]}, {Group_A_pick["country"]}")
    groupA_followers = Group_A_pick["follower_count"]

    #Group B
    Group_B_pick= data[Group_B] #data[index]
    print(f"Against B: {Group_B_pick["name"]}, {Group_B_pick["description"]}, {Group_B_pick["country"]}")
    groupB_followers= Group_B_pick["follower_count"]

    user_choice= input("Who has more followers, A or B: ").upper()
    Score= compare(groupA_followers, groupB_followers, user_choice,Score) #putting arguments

    if groupB_followers>groupA_followers:
        Group_A=Group_B #index of B will shift/saved to Group_A
        # Group B consist the random celebrity
        Group_B = random.randint(0, 49)
    elif groupA_followers>groupB_followers:
        Group_B = random.randint(0, 49) #As Group_A remains same, and the Group_B changes its value (stating: up against)



print(f"Sorry, that's wrong! Your Final Score: {Score}")



