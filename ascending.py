n=int(input())
lis=list(map(int,input().split()))
m=sorted(lis)
l=len(lis)
c=0
m1=len(m)
for i in range(0,l):
    if(lis[i]!=m[i]):
        c+=1
    if(c==1):
        print(i)
