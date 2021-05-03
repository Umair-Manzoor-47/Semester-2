numbers = []
count = 0
count = int(count)
# taking input
while count != 20:
    numbers.append(input("Enter number : "))
    count += 1

sum = 0
sum = int(sum)
# adding numbers
for i in range(0, 20):
   sum = int(numbers[i]) + sum

print("Sum of numbers is :", sum)