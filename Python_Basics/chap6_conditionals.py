#used for making decisions based on certain conditionals being
#suppose you have something like this
# your input goes thorough all if conditions even if it is true or false
# but elif once true for one condition breaks there itself

age = int(input("Enter your age : "))
#if statement 1 no else
if (age%2 == 0):
    print("age is even")
#end of if statement 1
#if statement number 2 has elif and else
if (age >=18):
    print("Your age is above age for consent")
elif (age < 0):
    print(" Negative input invalid")
elif (age == 0):
    print("0 age not allowed")
else:
    print("your age is below the age of consent")
# end of if statement 2
# remember if can be alone but elif or else can't be alone
