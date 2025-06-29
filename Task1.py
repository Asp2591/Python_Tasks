''' 
Find the Missing Number in an Array
A list contains n distinct numbers taken from 0, 1, 2, ..., n, but one number is
missing.
Write a function to find the missing number.
def find_missing_number(arr: list) -> int:
pass
Example:
arr = [3, 0, 1]
print(find_missing_number(arr)) 
Output: 2
'''

#Solution first approach 
arr = [3, 0, 1]
#Function starts
def find_missing_number(arr: list) -> int:
    #for loop to map all the elements in list
    for i in range(len(arr)):
        if i not in arr:        #if condition is for whether the number is list or not
            return i            #if number is not in list it will return that number which will our missing number

        

#Solution:second approach 

def find_missing_number(arr: list) -> int:
    n=len(arr)

    expected_sum= (n*(n+1))//2      # Using formula for sum of 'n' natural numbers
    actual_sum=sum(arr)
    missing_value=expected_sum-actual_sum
    return missing_value

print(find_missing_number(arr))



