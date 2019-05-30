n,k=list(map(int,input().split()))
for i in range(n,k):
    c=0
    for j in range(1,1000):
        if(i%j==0):
            c+=1 
        else:
            continue
    if c==2:
        print(i,end=" ")
print(" ")
