merit = [4,6,5,23,45]
sorted_merit = []
sorted02 = []
# making copy for sorting
for i in range(0, len(merit)):
    sorted_merit.append(merit[i])
    sorted_merit[i] = float(sorted_merit[i]) 

for i in range(0, len(merit)):
    largest = sorted_merit[0]
    largestidx = 0
    for j in range(0, len(merit)):
      if sorted_merit[j] < float(largest):
        largest = sorted_merit[j]
        largestidx = int(largestidx) 
        largestidx = j
    sorted_merit[largestidx] = 10000
    sorted02.append(largestidx)

counter = 0
counter = int(counter)
for i in range(0, len(merit)):
  counter = sorted02[i] 
  print(merit[counter])
