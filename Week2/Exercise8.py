# Write all file content into new file by skiping line 5 from following file
# test.txt file:				newFile.txt should be
# Line1				line1
# Line2				line2
# Line3				line3
# Line4				line4
# Line5				line6
# Line6				line7
# Line7
try:
    f = open("test.txt")
    f1 = open("newFile.txt", 'w')
    x = 1
    for line in f:
        if not x == 5:
            f1.write(line)
        x += 1



finally:
    f.close()
    f1.close()