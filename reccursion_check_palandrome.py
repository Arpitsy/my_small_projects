def pal(a):
    if a[0]==a[-1]:
        return pal(a[1:-1])
        
pal("madam")    
if len(pal())==0 or len(pal())==1:
    print("its a palandrome no")
else:
    print("Its not a palandrome no")
