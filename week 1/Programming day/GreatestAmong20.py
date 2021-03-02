numbers = []
count = 0
count = int(count)

# taking input
while count != 20:
    numbers.append(int(input("Enter number : ")))
    count += 1

numbers.sort(reverse=True) # this will sort the list  in decending order
print("Greates among 20 is", numbers[0]) # showing the greatest
