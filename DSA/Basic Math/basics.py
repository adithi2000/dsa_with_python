# Finding number of digits in a number
# def count_digits(n):
#     n= str(n)
#     return len(n)

# # def count_digits(n):
# #     count = 0
# #     while n>0:
# #         n //=10
# #         count +=1
# #     return count

# print(count_digits(123456789))
# # Output: 9
# def reverse_number(n):
#     rev = 0
#     while n>0:
#         rev = rev * 10 + (n %10)
#         n //=10
#     return rev

# n= int(input("Enter a number: "))
# rev=reverse_number(n)
# if rev == n:
#     print("The number is a palindrome")
# else:
#     print("The number is not a palindrome")
# # Output: 987654321

# def gcd(a,b):
#     divisor = min(a,b)
#     dividend = max(a,b)
#     while divisor !=0:
#         remainder = dividend % divisor
#         dividend = divisor
#         divisor = remainder
#     return dividend
# # n= int(input("Enter a number: "))
# print(gcd(10,15))
# from math import sqrt
# def divisors(n):
#     for i in range(1,int(sqrt(n)+1)):
#         if n % i ==0:
#             print(i, end=' ')
#             if i != n // i:
#                 print(n // i, end=' ')
# def divisors(n):
#     i=1
#     while i*i <= n:
#         if n % i ==0:
#             print(i, end=' ')
#             if i != n // i:
#                 print(n // i, end=' ')
#         i +=1
# divisors(36)
# def isPrime(n):
#     i=2
#     while i*i <= n:
#         if n % i ==0:
#             return False
#         i +=1
#     return True
# print(isPrime(25))
from math import log10,floor
def count_digits(n):
    if n== 0:
        return 1
    return(floor(log10(n)+1))
print(count_digits(123456789))
# Output: 9