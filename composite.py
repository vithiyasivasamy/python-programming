lim=int(input())
c=0
for i in range(1,lim):
    if(lim%i==0):
        c+=1
    else:
        continue
if(c==1):
    print("no")
else:
    print("yes")
