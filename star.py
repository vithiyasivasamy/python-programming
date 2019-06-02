sem=input()
l=len(sem)
if (l%2!=0):
    n=l//2
    for i in range(l):
        if i!=n:
            print(sem[i],end="")
        else:
            print("*",end="")
else:
    n=l/2
    for i in range(l):
        if i!=n and i!=n-1:
            print(sem[i],end="")
        else:
            print("*",end="")
