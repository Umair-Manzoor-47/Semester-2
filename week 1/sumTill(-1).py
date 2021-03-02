sum = 0
# taking input
num = int(input("Enter number : "))

#setting condition for while loop
while num != -1 :
    sum += num
    num = int(input("Enter number : "))

print("Sum of numbers is : ", sum)