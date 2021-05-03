# list
numbers = []
count = 0
count = int(count)

# taking input
while count != 24:
    numbers.append(input("Enter number : "))
    count += 1

for i in range(0, len(numbers)):
    if int(numbers[i])%2 != 0 and int(numbers[i])%5 == 0:
        print(numbers[i])
