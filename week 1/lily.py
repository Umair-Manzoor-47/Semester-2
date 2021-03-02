#taking input
age = int(input("Enter age of lily:"))
price = float(input("Enter price of a toy:"))
machine = float(input("Enter price of washing machine:"))

toys = 0 # counter to count toys
toys = int(toys)
for i in range(1, age+1, 2):
    toys += 1

FT = toys*price #calculating price of toys
money = 0
#calculating dollars 
for i in range(2, age+1, 2):
    money += 1

x = 0 # savings  
l = 0

for i in range(1, money+1):
    x = x+10
    l = l+x

total = l+FT #saved money
total = total-money
print("total =", total)

#results
if machine > total:
    print("The money is not enough")
else:
    print("She can buy the machine")
