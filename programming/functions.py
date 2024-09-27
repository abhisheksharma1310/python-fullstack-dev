#function
#function defintion
def fun_name(name = ""):
    print("You called me", name)
    return 1

#function call
x = fun_name()
print(x)

name = input("Enter name: ")
fun_name(name)

def is_even(num):
    if (num % 2) == 0:
        return True
    else:
        return False
    
print(is_even(2))

#recursion
def count_down(x):
    if x == 1:
        print(x)
        return 1
    print(x)
    return count_down(x-1)
count_down(9)

#lambda expression anonymous
lan = lambda arg1 : arg1*2
print(lan(2))

def calculate_len(str):
    i = 0
    for c in str:
        i += 1
    return i
print(calculate_len(name))