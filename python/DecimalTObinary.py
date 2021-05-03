# taking input
num = int(input("Enter number to find it's binary value : "))
decimal = int(num)
result = ""
# converting into binary using % finder
while decimal != 0:
    remainder = decimal % 2
    result += str(remainder)
    decimal = int(decimal/2)

final = result[::-1]  # list will be reversed
print("Binary number is : ", final)
