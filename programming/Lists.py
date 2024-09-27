#lists collection of similar items
temperatures = [234, 55, 233, 123, 23, 44]
print(len(temperatures))

#multidimension list
temp_with_centi = [[275, 2], [273,0], [23, 56]]
t1_c = temp_with_centi[0][1]
print(t1_c)

#spread operator
print(*temperatures)
print(*temp_with_centi)

