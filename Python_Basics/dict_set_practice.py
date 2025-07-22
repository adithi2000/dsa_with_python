# words = {
#     "madad" :"Help",
#     "kursi" : "Chair",
#     "billi" : "cat",
#     "kutta" : "dog",
#     "chai" : "tea"
# }

# word= input("Enter the word you want to search for : ")
# print(words.get(word.lower(),"Not present"))

# s = set()
# for i in range(0,8):
#     j=int(input(" Enter number of your choice : "))
#     s.add(j)
# print(s) # uniqu number input printed

# sets = {18, '18'}
# print(sets) #output { 18, '18'} , 18 and '18' are considered different

# sets = {18, 18.0, '18'}
# print(sets) #output { 18, '18'}  reason uses == and evaluates the numerical value, not datatype

# sets = {18, 18.5, '18'}
# print(sets) #output { 18, '18', 18.5}

#  if s= {} the s is dictionary not set, empty set s=set()

# dicto = {}

# for i in range(0,4):
#     name= input(" enter name : ")
#     prog= input(" enter prog name you like : ")
#     dicto.update({name : prog})

# print(dicto) # no issues as update() function is there but value will be the latest one entered for that key
# dicto['bhalu'] ="c"
# print(dicto) #output {'a': 'java', 'b': 'python', 'c': 'assembly', 'd': 'c#', 'bhalu': 'c'}

#problem 7
# s = {8,7,12,"Harry",[1,2]}
# print(s[4]) # sets are not hashable error TypeError: unhashable type: 'list'

