def finoacci(n):
    if n <= 1:
        return n
    else:
        return finoacci(n - 1) + finoacci(n - 2)
print(finoacci(5))  # Example usage, should return 5