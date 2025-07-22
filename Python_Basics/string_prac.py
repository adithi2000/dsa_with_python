# name= input("Please enter your name : ")
# #rint(f"Good Afternoon {name}")  # Greet the user with their name
# # output: 
# # Please enter your name : Adithi
# # Good Afternoon Adithi

# letter = f''' Dear <Name>
#             You are selected!
#             Thanks & Regards
#             Adithi  
#             <date> '''
# # letter = letter.replace("<Name>", name)
# # letter = letter.replace("<date>", "21-07-2025")
# #chaining
# letter = letter.replace("<Name>", name).replace("<date>", "21-07-2025")
# print(letter)  # Print the formatted letter

# name= "My Name is   Adithi" #this is a new string not the old name variable, the value exists in memory without a pointer
# if name.find("  ") > 0:
#     name = name.replace("  ", "")  # Replace double spaces with single space
# print(name)  # Print the modified name

letter = "Dear Harry, \n This Python course is nice! \n Thanks! \n"
print(letter)
