
def factorial(n):
    assert type(n) == int
    assert n>=0

    if (n==0 or n==1):
       return 1
    else:
        return factorial(n-1)*n

def variacion(n,m):
    assert n>=0
    assert m>=0

    assert type(n) == int
    assert type(m) == int
    return factorial(m)/factorial(n-m)

def permutacion(n):
    assert type(n) == int
    assert n>=0

    return factorial(n)

def convinatoria(n,m):

    assert n>=0
    assert m>=0
    assert type(n) == int
    assert type(m) == int
    return variacion(n,m)/permutacion(n)
