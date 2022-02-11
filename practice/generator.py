l = list((i**3 for i in range(5)[::-1]))
print(l)

data = 'golf'
sl = list(data[i] for i in range(len(data)-1, -1, -1))
print(sl)