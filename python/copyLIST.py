# list
list1 = ["ali", "", "khan", "ahmend", "", "Tanveer", ""]
list2 = []

count = 0
count = int(count)
# copying list 1 int list 2
for i in range(0, len(list1)):
    if list1[i] != "":
        list2.append(list1[i])
        count += 1

print(list2)