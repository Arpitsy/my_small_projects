a=input("Write here")    
if int(a)%3==0:
    n=len(a)
    print((n*(n+1))/2)
else:
    print("Invalid Number")
a=input("Write here ")
if len(a)>=5 and a[0].isalpha() and a[len(a)-1].isdigit():
    print("Valid")
else:
    print("Invalid")
