'''
Find Kth Largest Element in an Array
Given an unsorted list and an integer k, find the k-th largest element in the list.

def find_kth_largest(nums: list, k: int) -> int:
pass
Example:
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_largest(nums, k)) Output: 5

'''
#flow of program
'''
1. Sort the list in descending order.
2. Using condition return [k-1]th element.
'''
nums = [3, 2, 1, 5, 6, 4]
1,2,3,4,5,6
def find_kth_largest(nums: list, k: int) -> int:
    nums.sort()  
    return nums[-k]


print(find_kth_largest(nums,2))











