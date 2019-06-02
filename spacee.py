str=input()
l=len(str)
for i in range(0,l):
    if(i%2==0):
        print(str[i],end="")
print(" ",end="")
for i in range(0,l):
    if(i%2!=0):
        print(str[i],end="")
