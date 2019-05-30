n=list(map(int,input().split()))
y=n[0]
x=n[1]
z=n[2]
if (y>x and y>z):
    print(y)
elif (x>z):
    print(x)
else:
    print(z)
