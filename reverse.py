l=[[1, 2], [3, 4], [5, 6, 7]]
reversel=[]
def reverse(a):
    a=a[::-1]
    for i in a:
        if isinstance(i,list):
            b=i[::-1]
            reversel.append(b)
        else:
            reversel.append(i)
    return reversel
print(reverse(l))
