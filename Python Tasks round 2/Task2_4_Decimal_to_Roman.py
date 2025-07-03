'''
Decimal to Roman conversion
'''

#Approach 1
'''
Using library roman to convert by importing it

'''

# import roman
# num=3999
# def decimal_to_roman(num):
#     if num>=1 and num<=3999:
#         num=roman.toRoman(num)
#     else:
#         return 'Number is not between 1 to 3999'
#     return num


# print(decimal_to_roman(num))




#Approach 2

'''
Using list of fixed roman values of decimal numbers.
'''
num=1987
def decimal_to_roman(num):
    if num >= 1 and num <= 3999:
        roman_val_symb = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        romanStr = ''
        for val in roman_val_symb:
            count = num // val
            romanStr += roman_val_symb[val] * count
            num -= val * count

        return romanStr
    else:
        return "Number is not between 1 to 3999"


print(decimal_to_roman(num))


