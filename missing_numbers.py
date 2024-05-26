
'''
#MAANG Question

#Problem Statement 

Write a function to find the missing number in a given integer array of 1 to 100. 
The function takes to parameter the array and the number of elements that needs to be in array.  
For example if we want to find missing number from 1 to 6 the second parameter will be 6.

'''



#Solution 1

def missing_number(arr, n):
    # Calculate the expected sum of numbers from 1 to n
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the actual sum of elements in the array
    actual_sum = sum(arr)
    
    # The missing number is the difference between expected and actual sum
    return expected_sum - actual_sum

# Test the function
print(missing_number([1, 2, 3, 4, 6], 6))


#Using the arithmetic progression formula.
#To find the sum of the numbers from 1 to n
#Then subtract the sum of the numbers in the array to get the missing number.

# Solution 2

def missing_number(arr, n):
    # Calculate the sum of first n natural numbers
    total = n * (n + 1) // 2
    
    # Calculate the sum of numbers in the array
    sum_arr = sum(arr)
    
    # Find the missing number by subtracting sum_arr from total
    missing = total - sum_arr
    
    return missing
 
# Example
print(missing_number([1, 2, 3, 4, 6], 6))  # Output: 5


# Note : This function calculates the sum of the first n natural numbers using the arithmetic progression formula.
# Then subtracts the sum of the numbers in the array to find the missing number. 
# The time complexity of this function is O(n) because it iterates through the array once to calculate the sum of its elements.
