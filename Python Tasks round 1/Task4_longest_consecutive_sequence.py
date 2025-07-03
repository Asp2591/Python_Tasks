'''
Longest Consecutive Sequence
Given an unsorted list of integers, find the length of the longest consecutive
sequence.
def longest_consecutive(nums: list) -> int:
pass
Example:
nums = [100, 4, 200, 1, 3, 2]
1,2,3,4,100,200
print(longest_consecutive(nums)) Output: 4 (because [1,2,3,4] is the longest)

'''

nums = [0,1,2,3,5,6,7]

def longest_consecutive(nums: list) -> int:
    if not nums:
        return 0
    nums.sort()     #sorted the list
    maximum_streak = 1         #longest consecutive streak
    current_streak = 1         #current longest streak
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:  #finding duplicate numbers
            continue
        elif nums[i] == nums[i-1] + 1:  #finding ith index and (i+1)th index are consecutive
            current_streak += 1
        else:
            maximum_streak = max(maximum_streak, current_streak)  #whichever maximum or current streak would be maximum streak
            current_streak = 1      #restart the streak
    return max(maximum_streak, current_streak)  

print(longest_consecutive(nums))
