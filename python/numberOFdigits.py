number = int(input("enter number : "))
count = 0

# using while loop to count digit each time divided by 10
while number > 0:
    count += 1
    number = number // 10

print("Number of digits are : ", count)