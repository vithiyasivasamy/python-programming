def reverse(n):
    e=0
    while(n):
        rem=n%10
        e=e*10+rem 
        n=n//10
    return e 
n=int(input())
print(reverse(n))
