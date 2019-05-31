h,j=list(map(int,input().split()))
for i in range(h,j):
    o=len(str(i))
    sum=0
    t=i
    while(t>0):
       di=t% 10
       sum+=di**o
       t//= 10
    if i==sum:
        print(i,end=" ")
