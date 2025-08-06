''' pattern:
*****
*****
*****
*****
*****'''
# n = int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(n):
#         print("*",end=' ')
#     print("\n")

''' for pattern 
*
**
***
****
*****'''
# n= int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(i+1):
#         print("*", end='')
#     print("\n")

# n= int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(i+1):
#         print(j+1, end='')
#     print("\n")

# n= int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(i+1):
#         print(i+1, end='')
#     print("\n")

''' 
*****
****
***
**
*'''

# n= int(input("Enter the number of rows: "))
# for i in range(n,0,-1):
#     for j in range(i+1):
#         print("*", end='')
#     print("\n")

# n= int(input("Enter the number of rows: "))
# for i in range(n,0,-1):
#     for j in range(i):
#         print(j+1, end='')
#     print("\n")
''' 
      * 
     ***
    *****
   *******
  *********'''
# n= int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(n-i-1):
#         print("  ", end='')
#     for j in range(2*i+1):
#         print("* ", end='')
#     print("\n")

# # n= int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(i):
#         print("  ", end='')
#     for j in range(2*(n-i)-1):
#         print("* ", end='')
#     print("\n")

# n= int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(i+1):
#         print(((i+j)%2), end= ' ')
#     print("\n
n= int(input("Enter the number of rows: "))
for i in range(n):
    for  j in range(i+1):
        print(j+1, end=' ')
    print("  "*((n-i-1)*2),end='')
    for  j in range(i+1,0,-1):
        print(j, end= ' ') 
    print("\n")



