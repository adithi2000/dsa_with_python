#string functions

name="Adithi"
print(len(name)) #get length of string
print(name.endswith("thi")) #check if string ends with "thi"
print(name.startswith("A")) #check if string starts with "A"
print(name.capitalize()) #capitalize the first letter
print(name.upper()) #convert string to uppercase
print(name.lower()) #convert string to lowercase
print(name.find("di")) #find the index of substring "di"
print(name.replace("thi","ti")) #replace "thi" with "ti"
print(name.isalpha()) #check if all characters are alphabetic
print(name.isdigit()) #check if all characters are digits
print(name.isalnum()) #check if all characters are alphanumeric
print(name.islower()) #check if all characters are lowercase
print(name.isupper()) #check if all characters are uppercase
print(name.split("t")) #split the string at "t"
print(name.join("!")) #join the string with "!" between each character
print(name.strip()) #remove leading and trailing whitespace
name="this is a string"
print(name.title()) #convert the first character of each word to uppercase
print(name.count("i")) #count occurrences of "i"
print(name.index("is")) #find the index of the first occurrence of "is"
print(name.rfind("is")) #find the index of the last occurrence of "is"

#there are many more string functions available in Python
# you can explore them in the official Python documentation
# https://docs.python.org/3/library/stdtypes.html#string-methods
# or by using the help function in Python
# help(str) will give you a list of all string methods available
# or you can use dir(str) to see all attributes and methods of the string class
# you can also use the help function on a specific method
# help(str.upper) will give you information about the upper method

#output
# 6
# True
# True
# Adithi
# ADITHI
# adithi
# 1
# Aditi
# True
# False
# True
# False
# False
# ['Adi', 'hi']
# !
# Adithi
# This Is A String
# 3
# 2
# 5