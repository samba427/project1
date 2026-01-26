#program for hand cricket, a game we always play
import random
print("Hello hello... choose game mode pls... N for normal and C for crazy")
run_p=0
run_c=0
wicket_p=0
wicket_c=0

def crazy(side_p,side_c):
    print("hi")

def normal():
    print("well ig we are playing in normal mode then eh... choose O for odd and E for even")
    

toss_choice=input("O/E")
toss_option=["O","E"]
toss=random.choice(toss_option)
if(toss==toss_choice):
    print("choose whether you want to bat or bowl")
    side_p=input("bat or bowl")
    if side_p=="bat":
        side_c="bowl"
    else: side_c="bat"


choice=input("enter C or N")

if(choice=="C"):
    crazy(side_p,side_c)
else: normal()