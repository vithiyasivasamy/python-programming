sui,b=list(map(str,input().split()))
lis=list(map(int,input().split()))
c=0
for i in lis:
    if (i%2!=0):
        c+=1
        if(c==int(b)):
            print(i)
