first_number = 0
second_number = 0
third_number = 0

#taking input
first_number = int(input("Enter First Number :"))
second_number = int(input("Enter Second Number :"))
third_number = int(input("Enter Third Number :"))

#compairing 
if first_number > second_number and first_number > third_number:
    print("First number is gretest which is :", first_number)

if second_number > first_number and second_number > third_number:
    print("Second number is gretest which is :", second_number)
    
if third_number > second_number and third_number > first_number:
    print("Third number is gretest which is :", third_number)