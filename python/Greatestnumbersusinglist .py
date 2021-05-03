import os


os.system('cls' if os.name == 'nt' else 'clear')

numbers = []
count = 0

# taking input
while count != 5:
    numbers.append(int(input("Enter number : ")))
    count += 1

numbers.sort(reverse=True) # this will sort the list  in decending order
print("Greates among five is", numbers[0]) # showing the greates