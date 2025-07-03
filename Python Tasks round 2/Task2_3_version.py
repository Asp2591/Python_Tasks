'''
Version comparison
'''


# version1="1.01"
# version2="1.001"

def version_compare(v1,v2):
    ## Condition:revisons are compared using their int value ignoring leading zeros
    # we can compare 2 lists by their respective elemnts .

    ver1=list(map(int,v1.split('.')))  # split version in int format and stored in list
    # print(ver1)
    ver2=list(map(int,v2.split('.')))
    # print(ver2)

    # max_len is to calculate which version has shorter length so that we can add 0's at the last.
    max_len=max(len(ver1),len(ver2))
    # Adding zeros for shorter version

    ver1+=[0]*(max_len-len(ver1))
    ver2+=[0]*(max_len-len(ver2))

    # Condition verified as per question 

    if ver1 > ver2:
        return 1
    elif ver2 > ver1:
        return -1
    
    return 0

## Different versions to test
print(version_compare("1.01", "1.001"))      
# print(version_compare("2.0", "2.0.1"))       
# print(version_compare("3.0.33", "3.0.17"))   
# print(version_compare("0.2", "2.1"))        









