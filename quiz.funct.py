def quiz():
    count=-1
    money=0
    list1=["Zoro's surname ","Zoro's fav colour","What sword style does zoro use"]
    list2=["Roronoa","Green","Three sword style"]
    list3=[i.lower().strip() for i in list2]
    for i in list1:
        count+=1
        print(i) 
    
        ans=input("Write Your ans here ")
        if ans.lower().strip()==list3[count]:
           money+=1000
           print("Your ans is wright")
        else:
            print("Wrong ans")
    if money>=2000:
        print(f"You are filthy rich now, As you have won {money} Rupees😍")   
    else:
        print("Try again")   
quiz()
