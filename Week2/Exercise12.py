# Write a recursive function to calculate the sum of numbers from 0 to 10

def sumRecurse():
    return sumHelper(10)

def sumHelper(x):
    if x == 0:
        return 0

    return x + sumHelper(x - 1)

print(sumRecurse())