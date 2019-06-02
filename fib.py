def fib(n):
  if(n==0):
    return 0
  elif(n==1):
    return 1
  else:
    re=fib(n-1)+fib(n-2)
  return re
n=int(input())
for i in range(n+1):
  print(fib(i))
