list=['1','0']
str=input()
l=0
for i in str:
    if i in list:
        l+=1
if(l==len(str)):
    print("yes")
else:
    print("no")
