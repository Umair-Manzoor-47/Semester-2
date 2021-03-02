number = int(input("enter number : "))
power =  int(input("enter power : "))

count = 0
result = number
num = 0

while count != (power-1) :
    num = result
    result = number * num
    count += 1

print(result)