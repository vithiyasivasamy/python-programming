n,j=list(map(int,input().split()))
if(n<j):
    d=n 
else:
    d=j
for i in range(1,d+1):
    if(n%i==0 and j%i==0):
        g=i 
print(g)
