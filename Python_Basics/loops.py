# # loops are used to perform repeated actions
# #while loops
# count = 0
# while count < 5:
#     print("Count is:", count)
#     count += 1  # increment count by 1
# # While loop will stop when count is no longer less than 5, 
# # while loops are used when the number of iterations is not known beforehand

# #for loops
# for i in range(5):  # range(5) generates numbers from 0 to
#     # 4
#     print("Iteration number:", i)
# # For loops are used when the number of iterations is known beforehand
# # or when iterating over a sequence (like a list or string)
# # Example of iterating over a list
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print("Fruit:", fruit)
# # Example of iterating over a string
# word = "hello"
# for letter in word:
#     print("Letter:", letter)

# # wexample of while loop on a list
# numbers = [1, 2, 3, 4, 5]
# index = 0
# while index < len(numbers):
#     print(numbers[index])
#     index += 1  # increment index by 1

# # Example of using a for loop with a condition
# for i in range(10):
#     if i % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# range functions generates a sequence of numbers from start to stop-1 jumping by step size
# for i in range(start, stop, step)

# # Example of for loop with else
# # an optional else block can be used with for loops
# # else executed when the loop completes normally (not interrupted by a break statement)
# for i in range(1,3):
#     if i%2 ==0:
#         break
#     print("Iteration number:", i)
# else:
#     print("loop completed sucessfully")
# # The else block will not execute because the loop was interrupted by a break statement

#  break and continue and pass
# break statement is used to exit a loop prematurely
for i in range(5):
    if i == 3:
        break  # exit the loop when i is 3
    print("Current number:", i)

# continue statement is used to skip the current iteration and continue with the next one
for i in range(5):
    if i == 3:
        continue  # skip the rest of the loop body when i is 3
    print("Current number:", i)

# pass statement is a null operation, it does nothing
# it is used when a statement is syntactically required but no action is needed
