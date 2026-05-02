count=0
while count<4:
    passward="zoro123"
    a=input("Write the pass here")
    count+=1
    if a.strip()==passward:
        print("Acces granted")
        break
    if a.strip()!=passward:
        print("Wring pass, You have only",3-count,"Tries left")
    if count==3:
        break
