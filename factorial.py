def fact(n):
    if(n==1):
        return 1
    elif(n==0):
        return 1
    else:
        res=fact(n-1)*n
    return res 
n=int(input())
print(fact(n))




