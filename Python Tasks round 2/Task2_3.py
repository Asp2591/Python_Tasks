'''
Decimal to Roman conversion
'''

#Approach 1
'''
Using library roman to convert by importing it

'''

import roman
num=1956
def decimal_to_roman(num):
    num=roman.toRoman(num)
    return num


print(decimal_to_roman(num))




#Approach 2

'''
Using list of fixed roman values of decimal numbers.
'''
num=1956

def decimal_to_roman(num):
    val=[
        1000,900,500,400,100,90,50,40,10,9,5,4,1
    ]
    romanSymb=[
        'M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I'
    ]
    romanStr=''
    i=0
    while num > 0:
        count=num//val[i]                #1=6//5
        romanStr+=romanSymb[i]*count     #'MCDLV'='MCDLVI'*1
        num-=val[i]*count                  # 1456=6-(5*1)=1
        i+=1                            #i=10

    return romanStr

print(decimal_to_roman(num))


