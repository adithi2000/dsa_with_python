# marks = { "Adithi": 100, "karthikeya" : 120, "burger" : 10}
# print( marks, type(marks))
# print(marks['Adithi']) --> faster lookup O(1)

# this is a better approach that list of lists
# for any key we can have any value
# mutable in terms of values only, unordered, indexed, no duplicate keys

# dictionaris, tuples, sets, list all are nestable

#key value pairs can have mixed datatypes

marks = { 0:12,"Adithi": 100, "karthikeya" : 120, "burger" : 10}

# print(marks.items()) 
# print(marks.keys())
# print(marks.values())

# marks.update({"Harry" : 99}) #mutability of dictionary
# marks[0]=1200

# print(marks.get("Adi", "Not Available")) # should print not available or None by default
# print(marks["Adi"]) # error raised

print(marks.pop(0))
print(marks.popitem())
print(marks.pop(4,12)) #12 is default value if key 4 doesn't exists