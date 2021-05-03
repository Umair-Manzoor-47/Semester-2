numbers = []
count = 0
count = int(count)

# taking input
while count != 10:
    numbers.append(int(input("Enter number : ")))
    count += 1

numbers.sort(reverse=True) # this will sort the list  in decending order
print("2nd largest is", numbers[1]) # showing the greatest