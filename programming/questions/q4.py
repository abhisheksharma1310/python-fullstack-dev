# Loops - (ii)
# Write a function find_max(arr) that takes in a list of numbers and finds the maximum number. Please do not use the max() method provided by python. Using loops, iterating over the list find the maximum number.

# Note: Do not call the function or print anything here. It may not be accepted. You can do that on your local machine, of course.


def find_max(arr):
    #write your code
    max = 0
    for n in arr:
        if n > max:
            max = n
    return max

print(find_max([23,45,64, 12, 47, 90,5,8]))