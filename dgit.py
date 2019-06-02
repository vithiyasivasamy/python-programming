nm=list(input())
l=[]
for i in nm:
    if i.isnumeric():
        l.append(i)
if l==[]:
    print()
else:
    for i in l:
        print(i,end='')
