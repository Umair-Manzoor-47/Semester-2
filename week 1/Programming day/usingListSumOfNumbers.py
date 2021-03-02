numbers = []
count = 0
count = int(count)
# taking input
while count != 10:
    numbers.append(input("Enter number : "))
    count += 1

sum = 0
sum = int(sum)
# adding numbers
for i in range(0, 10):
   sum = int(numbers[i]) + sum

print("Sum of numbers is :", sum)