def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n-1) + fib(n-2)

def factorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial(n-1)

for n in range(0, 10):
    print(n, "->", fib(n))

print()

for n in range(0, 10):
    print(n, "->", factorial(n))
