multiple = 1
# taking input
number = int(input("Enter number to find factorial : "))

# printing factorial
for i in range(1, number+1):
    multiple = i * multiple

print("Factorial is :", multiple)
