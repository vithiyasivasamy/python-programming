lim=['a','A','e','E','i','I','o','O','u','U']
str=input()
c=0
for i in str:
    if i in lim:
        c+=1 
if(c>=1):
    print("yes")
else:
    print("no")
