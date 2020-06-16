# Write a function calculation() such that it can accept two
# variables and calculate the addition and subtraction of it.
# And also it must return both addition and subtraction in
# a single return call

def calculation(a, b):
    list = []
    list.append(a+b)
    list.append(a-b)
    return list

print(calculation(3, 4))