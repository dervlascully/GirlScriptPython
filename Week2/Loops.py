# WHILE LOOP
# With the while loop we can execute a set of statements as long as a condition is true.

# basic while loop
i = 1
while i < 6:
  print(i)
  i += 1

# while loop with break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#while loop with continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue # skips to next iteration (doesn't execute print(i))
  print(i)

# while loop with else
i = 1
while i < 6:
  print(i)
  i += 1
else:     # With the else statement we can run a block of code once when the condition no longer is true
  print("i is no longer less than 6")

# FOR LOOP
# A for loop is used for iterating over a sequence
# (that is either a list, a tuple, a dictionary, a set, or a string).

# basic for loop - looping through a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# looping thorugh a string
for x in "banana":
    print(x)

# break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break;
             # prints apple banana

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
             # prints apple

# continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
                # prints apple cherry

# range
# The range() function returns a sequence of numbers, starting from 0 by default,
# and increments by 1 (by default), and ends at a specified number.

for x in range(6): # Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
  print(x)

# range ( start, end, increment value)

for x in range(2, 30, 3):
  print(x)


# NESTED LOOPS

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

