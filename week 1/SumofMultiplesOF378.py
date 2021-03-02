total = 0
total = int(total)
i = 0
# using loop to find sum of multiples till 5000
while total < 5000:
    mul_1 = i * 3
    mul_2 = i * 7
    mul_3 = i * 8
    sum = int(mul_1) + int(mul_2) + int(mul_3)  # adding multiples
    total += int(sum)
    i += 1

# printing total sum
print("sum of multiples is :", total)
