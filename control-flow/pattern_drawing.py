""" size = int(input("Enter the size of the pattern: "))
while size !=0:
    for x in range(1, size):
        print("*"*size, end="")

    size = size - 1 """


# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop for each row
while row < size:
    # For loop for each column
    for col in range(size):
        print("*", end="")  # print * without newline
    print()  # move to next line after finishing one row
    row += 1
