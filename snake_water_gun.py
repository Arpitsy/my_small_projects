set={"snake","water","gun","snake","water","gun","snake","water","gun","snake","water","gun","snake","water","gun","snake","water","gun","snake","water","gun","snake","water","gun","snake","water","gun","snake","water","gun","snake","water","gun","snake","water","gun","snake","water","gun","snake","water","gun","snake","water","gun","snake","water","gun","snake","water","gun",}
comp=0
name=input("Enter Player Name ")
player=0
import random
while player<3 and comp<3:
    pop=random.choice(list(set))
    z=input("Choose your move ")
    if z.lower().strip()==pop:
        print("Its a Tie this time you just got damn lucky")
    elif z.lower().strip()=="snake" and pop=="water" or z.lower().strip()=="water" and pop=="gun" or z.lower().strip()=="gun" and pop=="snake":
        player+=1
        print("You won this one but next time y will not")
        print(name, " = ", player)
        print("Computer = ",comp)
    else:
        comp+=1
        print("Did y see that y brat i won this one and will win the next one too😈")
        print(name, " = ", player)
        print("Computer = ",comp)
if player>comp:
    print("You have won", name, "Congrats")
else:
    print("The outcome was inevitable you did'nt had a chance from the start😈")
    print("The player has Lost the game")

