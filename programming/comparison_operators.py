n1 = 5
n2 = 10
#greater than
n1_gt_n2 = n1 > n2
print(n1_gt_n2)
#less than
n1_lt_n2 = n1 < n2
print(n1_lt_n2)
#equal to
n1_eq_n2 = n1 == n2
print(n1_eq_n2)
#not equal to
n1_neq_n2 = n1 != n2
print(n1_neq_n2)

password = int(input("password "))
correct_pass = 12345
if password == correct_pass:
    print("correct password")
else:
    print("incorrect password")