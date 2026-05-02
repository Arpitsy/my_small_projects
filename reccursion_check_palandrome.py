def pal(a):
    if a[0]==a[-1]:
        return pal(a[1:-1])
