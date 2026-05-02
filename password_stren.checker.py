a=input("Write Yours Password Here")
c=any(b.isdigit() for b in a )
if len(a)>=8 and c and "@" in a:
    print("Strong Password")
elif len(a)>=8 and c or len(a)>=8 and "@" in a or "@" in a  and c :
    print("Average Password")
elif len(a)>=8 or c or "@" in a :
    print(" Weak Password")
else:
    print("Bruh Write Something Y Are Very LIkly To get Hacked") 
