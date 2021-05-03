#list
list1 = [2,4,3,1,9,7,8,6]

sum = 0
sum = int(sum)
# adding numbers
for i in range(0, len(list1)):
   sum = int(list1[i]) + sum

average = int(sum) / len(list1)
print("Average value is : ", average)