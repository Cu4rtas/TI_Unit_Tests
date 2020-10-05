def factorial(n):
    '''
    Returns the value of the number passed in the "n" param
    '''
    if n == 0: return 1
    return factorial(n-1)*n

def exponencial(x,n):
    """
    Returns the value of the exponencial function evaluated in "x"
    and with "n" digits of exactitude
    """
    if n < 0: return "Sorry, no numbers below zero"
    return 1 if n == 0 else exponencial(x,n-1) + (x**n)/factorial(n)

