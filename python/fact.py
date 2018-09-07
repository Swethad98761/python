def fact(a):
  i=1
  for j in range(1,a+1):
    i=i*j
  return i

a=int(input())
print(fact(a))


