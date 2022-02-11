# a, b = 0, 1

# while a < 1000:
#     print(a, end=',')
#     a, b = b, a + b

    
# rangeはiterableでリストではない

# a= ['mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])
    
# for i in range(5):
#     if (i == 3):
#         pass
#     else:
#         print(i)
        
# 関数

# def fib(n):
#     a, b = 0, 1
    
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b

# fib(100)
# fib(5000)


def ask_ok(pronpt, retries=4, reminder='try again!'):    
    while retries > 0:
        ok = input(pronpt)
        if ok in ('y', 'ye', 'yes'):
            break
        if ok in ('n', 'no'):
            retries -= 1
            if retries <= 0:
                raise ValueError('invalid user responce')
            print(reminder)
        
ask_ok('Do you really wanna quit?', retries=8, reminder='oh reallry?')
