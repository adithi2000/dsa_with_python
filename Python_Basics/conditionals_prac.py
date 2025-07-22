# #greatest of 4 numbers
# num1= int(input("Enter number 1 : "))
# num2=int(input("Enter number 2 : "))
# num3= int(input("Enter number 3 : "))
# num4= int(input("enter number 4 : "))

# if( num1 > num2 and num1 > num3 and num1 > num4):
#     print(f"greatest number is {num1}")
# elif( num2 > num1 and num2 > num3 and num2 > num4):
#     print(f"greatest number is {num2}")
# elif( num3 > num2 and num3 > num1 and num3 > num4):
#     print(f"greatest number is {num3}")
# else:
#     print(f"greatest number is {num4}")

# # marks of 3 subjects
# sub1= int(input("Enter marks of subject 1 : "))
# sub2=int(input("Enter marks of subject 2 : "))
# sub3= int(input("Enter marks of subject 3 : "))

# percent= (sub1+sub2+sub3)/3

# if( sub1 >=33 and sub2 >=33 and sub3 >= 33 and percent >=40 ):
#     print(f"pass and percentage is {percent}")
# else: 
#     print(f"fail as percent is {percent}")

# spam_list= ['make a lot of money','buy now','subscribe this','click this']
# msg = input("Enter message you want to check : ")
# flag = False
# for i in spam_list:
#     if i in msg:
#         print("Spam")
#         flag= True
#         break
# if(flag == False):
#     print("not spam")

# username = input("Enter username :  ")
# if (len(username) > 10):
#     if(" " in username or "  " in username):
#         print("No 10 characters , used spaces in between")
#     else:
#         print("Valid username")
# else:
#     print("Characters less than 10")

# # name in list
# names=["Harry","Shubam","Divya","Adithi","Karthikeya"]
# name= input("Enter your name : ")
# if( name.capitalize() in names):
#     print("Name is list")
# else:
#     print("name not in list")

## is given post talking about harry
post = input("Enter post : ")
if("Harry".lower() in post.lower() ):
    print("Post talks about harry")
else:
    print("Post doesn't talk about harry")