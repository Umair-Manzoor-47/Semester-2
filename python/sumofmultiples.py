# taking input
val_1 = int(input("Enter first number : "))
val_2 = int(input("Enter 2nd number : "))
mul = int(input("Enter number till find multiple : "))

mul_1 = 0
mul_2 = 0
sum = 0
total = 0
# finding multiples
for i in range(1, mul+1):
    mul_1 = i * val_1
    mul_2 = i * val_2
    sum = int(mul_1) + int(mul_2) #adding multiples
    total += sum  

print("sum of multiples is :", total)
