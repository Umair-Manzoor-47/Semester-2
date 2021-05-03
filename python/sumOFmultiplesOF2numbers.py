number01 = 0 #Defining numbers
number02 = 0

number01 = input("Enter First number to find Multiples : ") 

"""Multiplying and Saving Multiples of First number into variables """
mul01 = (int(number01) * 1)
mul02 = (int(number01) * 2)
mul03 = (int(number01) * 3)
mul04 = (int(number01) * 4)
mul05 = (int(number01) * 5)

number02 = input("Enter Second number to find Multiples : ")
"""Multiplying and Saving Multiples of 2nd number into variables"""
SECmul01 = (int(number02) * 1)
SECmul02 = (int(number02) * 2)
SECmul03 = (int(number02) * 3)
SECmul04 = (int(number02) * 4)
SECmul05 = (int(number02) * 5)

#Adding & Showing the sum of Multiples
print("Sum of Multiples of ", number01, "and", number02, "Are :")
print(int(mul01) + int(SECmul01))
print(int(mul02) + int(SECmul02))
print(int(mul03) + int(SECmul03))
print(int(mul04) + int(SECmul04))
print(int(mul05) + int(SECmul05))