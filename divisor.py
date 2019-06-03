def divisible(num):
    if(num%2!=0):
        print (num)
    else:
        s=num//2
        divisible(s)
num=int(input())
divisible(num)
