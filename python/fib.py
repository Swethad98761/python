def fib(n):
  a=0
  b=1
  print(a,end=' ')
  c=1
  while c<=n:
    
    print(c,end=' ')
    c=a+b
    a=b
    b=c

n=int(input())
if n==1:
  print(0)
else:
  fib(n)


