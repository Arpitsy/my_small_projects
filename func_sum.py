def sum(a):
    
    c=0
    
    if len(a)==1:
        return(int(a))

    else:
        for i in a:
            c+=int(i)
        return c    


print(sum("345"))

