#create files
file = open("apples.text", "w")

#modes
# write "w"
def write_file(file_name, stuff):
    file = open(file_name, "w")
    file.write(stuff)
    file.close()

# reda "r"
def read_file(file_name):
    try:
        file = open(file_name, "r")
        stuff = file.read()
        print(stuff)
        file.close()
    except:
        print("Something went wrong")

# append "a"
def append_file(file_name, stuff):
    file = open(file_name, "a")
    file.write(stuff)
    file.close()

write_file("apples.text", "My name is Abhishek")
append_file("apples.text", "Hello!!")
read_file("apples.text")


password = "12345"
if len(password) < 8:
    raise Exception("The password must be greater than 8")