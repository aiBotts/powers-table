# This program displays a table of square and cubes for a specified range of numbers given by the user

# Get the starting value from the user
print('Table of Powers')
print()
start = int(input('Enter a Starting number: '))


# Get the end value from the user
end = int(input('Enter a Stop number: '))

# If the user puts in a lower stop number an error displays
while end < start:
    # Error message
    print('The Stop number cannot lower than the Starting number.  Please choose another number.')
    start = int(input('Enter a Starting number: '))

# Print the table headings
print()
print('Number\tSquared\tCubed')                     # Using \t for tabbing out the columns
print('======\t=======\t=====')

# Print the numbers and their squares and cubes
for number in range(start, end + 1):
    squared = number ** 2                           # Squaring the user's number
    cubed = number ** 3                             # Cubing the user's number
    print(number, '\t', squared, '\t', cubed)
