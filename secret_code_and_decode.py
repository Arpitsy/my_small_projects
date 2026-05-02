a={"a","b","c","d","e","f","G","h","i","j","K","l"}
q=""
for i in range(3):
    q+=a.pop()
w=""
for j in range(3):
    w+=a.pop()
num=input("Write Your No Here")
if len(num)>=3:
    d=num[1:len(num)]+ num[0]
    coded=q+d+w
    print(coded)
else:
    print(num[::-1])



#Decode 

if len(coded)>=3:
    c= coded[len(coded)-4]+coded[3:len(coded)-4]
    print(c)
else:
    print(coded[::-1])
