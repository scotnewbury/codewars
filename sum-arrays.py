# Write a function that takes an array of numbers and returns the sum of the numbers.
# The numbers can be negative or non-integer. If the array does not contain any 
# numbers then you should return 0.

# Examples
# Input: [1, 5.2, 4, 0, -1]
# Output: 9.2

# Input: []
# Output: 0

# Input: [-2.398]
# Output: -2.398

# Assumptions
# You can assume that you are only given numbers.
# You cannot assume the size of the array.
# You can assume that you do get an array and if the array is empty, return 0.

def sum_array(a):
    # The for loop could be replaced by the sum() function
    for i in range(len(a)):
        print(a[i])
    return(0)

numbers = (1, 5.2, 4, 0, -1)
print(sum_array(numbers))
