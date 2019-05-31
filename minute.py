n=int(input())
if(n<60):
    print("0",end=" ")
    print(n)
else:
    m=n//60
    y=60*m
    x=n-y
    print(m,end=" ")
    print(x)
