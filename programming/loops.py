#while loop
# i = 0
# while i < 10:
#     print(i)
#     i += 1

# i = 0
# while i < 10:
#     print(i)
#     i += 1
#     if i == 5:
#         break

# i = 0
# while i < 10:
#     print(i)
#     i += 1
#     if i == 5:
#         continue

# for loop
for i in range(10):
    print(i)

for i in range(5, 10):
    print(i)

for i in range(1, 10, 2):
    print(i)

numbers = [12, 23, 44, 34, 23, 45, 65, 76]
for n in numbers:
    print(n)

dictionary = {
    "name": "jacky",
    "state": "stable",
    "performance": 0.89
}

for k in dictionary:
    print(k, ":", dictionary[k])