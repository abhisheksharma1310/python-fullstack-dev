# Conditionals - (i)
# Grading Problem
# In this exercise you will have to write code that inputs marks between 0 and 100 of 5 different subjects. You have to print the grades (Letters) given the following criteria in the range of marks(inclusive)
# Marks : Grade
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# 50-59: E
# 0-49: F
# Example Input
# 56
# 67
# 34
# 76
# 98
# Example Output
# EDFCA
# Note: make sure to convert the input into integer!

marks = []
#taking in the input for 5 marks from the user and adding it to the list
for i in range(5):
    marks.append(int(input()))
# now that we have all the marks we can just loop over it
output = ""
for i in marks:
#Write your code here
#for every mark concatenate grades to the output e.g output+="A"
    #start here
    if i >= 90 and i <= 100:
        output += "A"
    elif i >= 80 and i <= 89:
        output += "B"
    elif i >= 70 and i <= 79:
        output += "C"
    elif i >= 60 and i <= 69:
        output += "D"
    elif i >= 50 and i <= 59:
        output += "E"
    elif i >= 0 and i <= 49:
        output += "F"
#now we simply print the output
print(output)
