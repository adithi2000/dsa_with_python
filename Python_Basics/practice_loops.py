# multiplication table of 5
# for i in range(1,11):
#     print(f" 5 X {i} = {5*i}")

# # greet all list members whose name starts with s
# lists= ['harry','soham','sachin','rahul']

# for i in lists:
#     if i.startswith('s'):
#         print(f"Hello {i} !!!")

# # tables with while loop
# i=1
# while i < 11:
#     print(f" 5 X {i} = {5 * i}")
#     i+=1

# # prime or not prime
# num = int(input("enter a number : "))
# for i in range(2,num):
#     if(num % i == 0):
#         print("Not prime")
#         break
# else:
#     print("Prime")

# # find sum of first n natural numbers

# num = int(input("enter a number : "))
# sum = 0
# i = 1
# while i <= num:
#     sum+=i
#     i+=1
# print(sum)

# #  factorial
# num = int(input("enter a number : "))
# fact = 1
# for i in range(1,num+1):
#     fact *= i
# print(fact)

# # star pattern printing
# ''''''
# num = int(input("enter a number : "))  
# for i in range(1,num+1):
#     print(" "*(num-i),end=' ')
#     print("*"*(2*i-1),end="\n")

# star pattern 2

# num = int(input("enter a number : "))
# for i in range(1,num+1):
#     print("*"*(i),end="\n")

# num = int(input("enter a number : "))
# for i in range(1,num+1):
#     for j in range(1,num+1):
#         if(i % 2 == 0):
#             if(j ==1):
#                 print("*", end=' ')
#             if(j == num):
#                 print("*", end="\n")
#             else:
#                 print(" ",end=' ')
#         else:
#             if(j == num):
#                 print("*", end="\n")
#             else:
#                 print("*",end=' ')
        
# # tables in reverse order
# num = int(input("enter a number : "))
# for i in range(10,0,-1):
#     print(f" {num} X {i} = {num * i}")

# tables in reverse order
num = int(input("enter a number : "))
for i in range(1,11):
    print(f" {num} X {11-i} = {num * (11-i)}")