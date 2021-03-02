# taking input
number = int(input("enter number : "))
counter = 0

# checking if divided more than 1 
for i in range(1, number) :
    if number % i == 0 :
        counter += 1

#printing if number id divided by more than 2 terms 
if counter >= 2 :
    print(number, " is a prime number")

else :
    print(number, " is NOT a prime number")
