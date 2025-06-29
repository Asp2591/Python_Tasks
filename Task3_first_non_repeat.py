'''
Find the First Non-Repeating Character
Given a string, return the first non-repeating character. If all characters repeat, return
"None".
def first_unique_char(s: str) -> str:
pass
Example:
s = "swiss"
print(first_unique_char(s)) Output: "w"

'''
s = "swiss"
def first_unique_char(s: str) -> str:
    char_count={}                   #This is the initialization of dictionary which store characters and respected count in key:value pair 
    for char in s:                  # for loop to find char and count
        if char in char_count:
            char_count[char]+=1     # It will count the number if already exist then count increases by 1
        else:
            char_count[char]=1      # else set to 1 and remains as it is

    for char in s:                  # This loop is to find which char has count 1 first time
        if char_count[char]==1:     
            return char


    return 'None is unique'         # if no unique char present it will return this statement
    
print(first_unique_char(s))












