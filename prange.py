c,w=map(int,input().split())
for i in range(c+1,w):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i,end=" ")
