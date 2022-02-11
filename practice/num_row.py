def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    
def fib_list(n):
    l = []
    a, b = 0, 1
    while a < n:
        l.append(a)
        a, b = b, a + b
        
    return l
