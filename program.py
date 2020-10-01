def factorial(n):
    if n == 0: return 1
    return factorial(n-1)*n

def exponencial(x,n):
    return 1 if n == 0 else exponencial(x,n-1) + (x**n)/factorial(n)

