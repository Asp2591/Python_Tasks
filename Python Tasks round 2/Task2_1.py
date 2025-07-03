# Disarium Number

'''
175
1^1+7^2+5^3=175
'''
def is_diasrium(num):
    total=0

    for i,n in enumerate(str(num),start=1):
        total+=int(n)**i
    return total==num

# num=int(input('Enter a number::'))
print(is_diasrium(175))




        