h,k=list(map(int,input().split()))
for i in range(h,k):
    o=len(str(i))
    sum=0
    r=i
    while(r>0):
       di=r% 10
       sum+=di**o
       r//= 10
    if i==sum:
        print(i,end=" ")
