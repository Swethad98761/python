squares = {}
for x in range(10):
   squares[x] = x*x
print(squares)
print(squares[2])
print(squares.keys())
print(squares.values())
print(squares.items())
d={1:1,2:2,False:3}
print(squares.pop(5))
print(len(d))
print(all(d))
print(any(d))
d.clear()
print(d)

