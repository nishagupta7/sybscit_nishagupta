def fib(n):
    a = 4
    b = 7
    if n == 5:
        print (a)
    else:
        print (a)
        print (b)
        for i in range (6,n):
            c = a + b
            a = b
            b = c
            print (c)
fib(10)
