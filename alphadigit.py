str=input()
f=0
g=0
for i in str:
    if i.isalpha():
        f+=1
    elif i.isnumeric():
        g+=1
if(f>=1 and g>=1):
    print("Yes")
else:
    print("No")
