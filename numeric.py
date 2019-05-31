l=['1','2','3','4','5','6','7','8','9','0','.']
str=input()
count=0
for i in str:
  if i in l:
    count+=1
if(count==0):
  print("yes")
else:
  print("no")
