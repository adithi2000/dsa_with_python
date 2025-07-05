#functional recursion example
def sumn(n):
    if n == 0:
        return 0
    else:
        return n+ sumn(n-1)
    
print(sumn(5))  # Output: 15

# parameterized recursion example
def sumnn(n,total=0):
    if( n == 0):
        print(total)
        return
    else:
        total += n
        sumnn(n-1,total)
sumnn(3)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120