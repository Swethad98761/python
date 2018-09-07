def rev(a):
  r=0
  c=0
  while a>0:
    #c+=1
    r=r*10+(a%10)
    a=int(a/10)
  return r

a=int(input())
print(rev(a))


