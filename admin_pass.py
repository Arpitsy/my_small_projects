a= "admin"
b="1234"
c=0
while c<3:
    d=input("Write the user id")
    e=input("Write the pass")
    print("Loop running, c =", c)
    if d==a and e==b :
        print("YOU have logged in succesfully")
        break
    else:
        print("Wrong input")
        c+=1
        if c==3:
           print("You have been lockd out")
