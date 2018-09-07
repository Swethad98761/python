def square(y):
  y[:]=(i**2 for i in y)
def sum1(a,b,c):
  c=a+b
  return c
print("pass by value")
a=5
b=6
c=0
print(sum1(a,b,c))
print(c)
print("pass by reference")
x=[5,4,3]
square(x)
print(x)
