# d= {} #empty dictonary
# print(type(d))

# #empty set
# d = set()
# print(type(d))
# li=[1,5,5,5,32,64,128]
# li.sort(reverse=True)
# print(li)
# d= set(li)
# print(d) #output [128, 64, 32, 5, 5, 5, 1]
#         # {128, 1, 32, 64, 5}

s= {128,1,32,64,5}
d= {1,2,3,4,5,7}
# s.add(566)
# s.remove(1)
# print(s.pop())
# print(s)

#operations on sets
# print(s.union(d))
# print(s.intersection(d))
# print(s.difference(d)) #s-d is s without s.intersection(d)
#output {128, 1, 32, 64, 2, 5, 3, 4, 7}
# {1, 5}
# {128,32,64}
print(s.issubset({1,2,3,4,5,6,7,8,9,10})) #false
#  Use repl to find out more on how different functions work
