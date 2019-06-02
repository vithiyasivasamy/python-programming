am,bm=map(int,input().split())
if am>bm:
	t=am
else:
	t=bm
while(1):
	if t%am==0 and t%bm==0:
		l=t
		break
	t+=1
print(l)
