def rev(a):
  r=0
  c=0
  while a>0:
    #c+=1
    r=(a%10)
    c=c+r
    a=int(a/10)
  return c

a=int(input())
print(rev(a))


