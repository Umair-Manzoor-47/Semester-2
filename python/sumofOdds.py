import os


os.system('cls' if os.name == 'nt' else 'clear')
sum = 0

# taking input
num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

# finding odds between two numbers and adding them
for i in range(num_1, num_2):
    if i % 2 != 0:
        sum += i

# printing the result
print("Sum of numbers is : ", sum)
