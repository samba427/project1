#simple rock paper scissors game... just abt as easy as it gets really
import random
print("welcome to rock paper scissors... lets get started shall we")

user_win=0
comp_win=0

ch=["r","s","p"]
flag=True
while flag:
    choice=input("enter r for rock or p for paper or s for scissors(q to quit): ")
    if(choice not in ["p","q","r","s"]):
        choice=input("please enter one of the valid choices ")
    csc=random.choice(ch)

    if choice!="q":
        if(csc=="r"):
            if(choice=="r"):
                print("draw")
            elif(choice=="p"):
                print("u win wooohooo")
                user_win+=1
            else:
                print("u loooose")
                comp_win+=1
        elif(csc=="p"):
            if(choice=="p"):
                print("draw")
            elif(choice=="s"):
                print("u win wooohooo")
                user_win+=1
            else:
                print("u loooose")
                comp_win+=1
        elif(csc=="s"):
            if(choice=="s"):
                print("draw")
            elif(choice=="r"):
                print("u win wooohooo")
                user_win+=1
            else:
                print("u loooose")
                comp_win+=1

    else: flag=False

print(f"final score is: user={user_win}, computer={comp_win}")
if(comp_win>user_win):
    print("guess ai is taking over after all")
elif(comp_win<user_win):
    print("woahhh thats crazy no way... ur going first when ai takes over")
else: print("it is what it is")








