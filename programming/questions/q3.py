# Functions - (i)
# Write a function that tests the validity of a password
# * the function checks whether the password has atleast 3 numbers
# * the length of the password is more than or equal to 8
# * the password contains atleast one uppercase and one lowercase letter e.g aF232515 is a possible password
# Function
# make sure the function is defined as is_password_valid(password)
# The function will return a boolean (True or False)
# Example Input
# "as235252" 
# Output
# False
# Other examples
# "2rAsr345" is valid so return True
# "fWevgaw42" is not valid (only 2 numbers)
# Note: Do not call the function here, only define it. You can try to solve this on your local machine and then put the solution here
# NOTE: use the isnumeric() function to figure out whether a character is a number or not
# example :
# >>>x = "2"
# >>>x.isnumeric()
# >>>True
# similar string methods: x.isupper() and x.islower()
# Assumptions
# We assume that user can't enter special characters to make the problem a little easier.

def is_password_valid(password):
    # your code goes here
    # check the solution in the discord server. 
    more_than8 = len(password) >= 8
    at_least3_num = 0
    upper_case = 0
    lower_case = 0
    for char in password:
        if char.isnumeric():
            at_least3_num += 1
        if char.isupper():
            upper_case += 1
        if char.islower():
            lower_case += 1
    print(at_least3_num >= 3, more_than8, upper_case, lower_case)
    return at_least3_num >= 3 and more_than8 and (upper_case >= 1) and (lower_case >= 1)


print(is_password_valid("2rAsr345"))


