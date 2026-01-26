#generic slot machine that we are used to seeing
import random
slot=["#","%","$","@","&"]
amt=100
q=True
while q:
    a=random.choice(slot)
    b=random.choice(slot)
    c=random.choice(slot)
    print("place your bets please")
    x=input("wanna play (x to exit)")
    
    if(x=="x"):
        print("thnx for playing")
        q=False
        continue

    bet=int(input("enter bet amountt: "))
    print(f"|{a}|{b}|{c}|")
    if(a==b==c):
        print("u win yayyy")
        amt+=bet*2
        print(f"ur balance is {amt}")
    else: 
        print("aww u lose")
        amt-=bet
        print(f"ur balance is {amt}")
    
    if(amt<=0):
        print("u broke boyy")
        q=False 

print(f"ur total winnings are {amt}")



