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

#Solution
arr = [3, 0, 1,2]
#Function starts
def find_missing_number(arr: list) -> int:
    #for loop to map all the elements in list
    for i in range(len(arr)):
        if i not in arr:        #if condition is for whether the number is list or not
            return i            #if number is not in list it will return that number which will our missing number
        return 'No missing'     #else return there is no missing value
        
print(find_missing_number(arr))