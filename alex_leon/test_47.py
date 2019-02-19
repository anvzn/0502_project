def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)



print(factorial(7))


def fib(n):
    if n<3:
        return 1
    return fib(n-1) + fib(n-2)
