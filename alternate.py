xv=str(input())
yv=list(xv)
yv[::2],yv[1::2] =yv[1::2],yv[::2]
print (''.join(yv))
