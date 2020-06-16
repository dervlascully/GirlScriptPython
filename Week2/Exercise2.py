# Print the following pattern
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


for y in range(1, 6):
    list = []
    for z in range (1, y + 1):
        list.append(z)
        
    print(list)