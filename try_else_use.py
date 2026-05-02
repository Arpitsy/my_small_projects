a=input("Write Your Num")         
try :
    b=int(a)
    for i in range (1,11):
        print(b*i)
except ValueError :
    print("Pls Write a Numb")      
