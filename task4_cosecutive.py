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
    nums.sort()
    longest = 1
    streak = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            continue
        elif nums[i] == nums[i-1] + 1:
            streak += 1
        else:
            longest = max(longest, streak)
            streak = 1
    return max(longest, streak)

print(longest_consecutive(nums))
