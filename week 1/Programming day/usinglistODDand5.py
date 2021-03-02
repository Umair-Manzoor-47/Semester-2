# list
numbers = []
count = 1

# taking input
while count != 10:
    numbers.append(input("Enter number : "))
    count += 1

for i in range(0, 9):
    if int(numbers[i])%2 != 0 and int(numbers[i])%5 == 0:
        print(numbers[i])
