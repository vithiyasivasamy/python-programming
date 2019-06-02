lim=input().split()
for i in lim:
	s=set(i)
	
	if len(s) == len(i):
		print("Yes")
	else:
		print("No")
