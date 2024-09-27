# Loops - (i)
# Does it have all vowels?
# Write a program that inputs two strings and finds out whether it(each) has all the vowels. Vowels are basic alphabets in English which make vowel sounds .(a,e,i,o,u)
# If the input string has all the vowels then print "YES" otherwise print "NO". There are many ways to solve this problem, make sure to really think about the solution and do it yourself by restricting yourself to only use loops, dictionaries, lists (the things we have studied before)
# Example Input #1
# This house is pretty
# There is a candy shop near the bridge for university students
# Example Output #1
# NO
# YES
# in the first sentence we dont have all the vowels {a,e,i,o,u} in the second one we have.
# Hint/remember: you can iterate over strings like lists.

text1 =  input()
text2 = input()
for text in [text1,text2]:
    #just iterating through them
    #Write your code here. for each text you have to print("YES") or print("NO") as described in the problem
    vowels = {'a', 'e', 'i', 'o', 'u'}
    found_vowels = set()
    for char in text.lower():
        if char in vowels:
            found_vowels.add(char)

    if vowels == found_vowels:
        print("YES")
    else:
        print("NO")
