#string are immutable
#list are mutable
#a list can be indexed just like a string
#lists are not necessarily homogeneous
# friends = ['Alice', 'Bob', 'Charlie', 'David']
# print(friends[:4:3])
# friends.append("eve")
# print(friends)
# l1=[21,19,34,22]
# l1.sort()
# print(l1)
# l1.reverse()
# print(l1)
# l1.insert(2, 25) #insert 25 into list such that it is at index 2
# print(l1)
# l1.remove(19)
# print(l1)
# print(l1.pop(2) )
#removes the element at index 2

#also ask chatgpt or copilot for more list methods

#tuples are immutable
#tuples are defined using parentheses

a = (1,2,2,5,6)
print(type(a))

#empty tuple
# b = ()

num=a.count(2)  # returns the number of occurrences of 2 in the tuple
print(num)

print(a.index(5)) # returns the index of the first occurrence of 5 in the tuple
print(a[:2]) # slicing the tuple to get the first two elements
# tuples can be unpacked
x, y, z, w, v = a  # unpacking the tuple into variables
print(x, y, z, w, v)  # printing the unpacked values
# tuples can also be concatenated
b = (7, 8, 9)
c = a + b  # concatenating two tuples
print(c)  # printing the concatenated tuple

#memebership test
print(2 in a)  # checking if 2 is in the tuple a



