import os


os.system('cls' if os.name == 'nt' else 'clear')  # clearing screen
# arrays(lists)
students = ["umair", "Ali", "Ahmed"]
matric = [1042, 1080, 1067]
fsc = [462, 480, 470]
ecat = [190, 250, 200]
merit = []
sorted_merit = []
bottom_up = []
# variables
Running = True
count = 0
count = int(count)

while Running == True:
    os.system('cls' if os.name == 'nt' else 'clear')  # clearing screen
    print("****************************************************************")
    print("             University Management System                       ")
    print("****************************************************************")

    # options
    print("1-Add student")
    print("2-View added Student")
    print("3-Top student")
    print("4-Bottom Student")
    print("5-Exit")
    opt = int(input("Enter your option:"))
    if opt == 5:
        Running = False
    if opt == 1:
        os.system('cls' if os.name == 'nt' else 'clear')  # clearing screen
        students.append(input("Enter Name : "))
        matric.append(input("Enter Matric marks : "))
        fsc.append(input("Enter FSC marks : "))
        ecat.append(input("Enter ECAT marks : "))

        # claculating percentages
        ecat_per = int(ecat[count])*30 / 400
        matric_per = int(matric[count])*25 / 1100
        fsc_per = int(fsc[count])*45 / 520

        # adding Percentages
        merit.append(float(ecat_per) + float(matric_per) + float(fsc_per))
        count += 1
        print("Student added.")
        input("press any key to continue...")

    if opt == 2:  # view added student
        os.system('cls' if os.name == 'nt' else 'clear')  # clearing screen
        # printing added students
        print("\t", "Name", "\t", "SSC", "\t",
              "FSc", "\t", "Ecat", "\t", "Aggregate")
        for i in range(0, len(merit)):
            print("\t", students[i], "\t", matric[i], "\t",
                  fsc[i], "\t", ecat[i], "\t", merit[i])

        input("press any key to continue...")

    # view top student first
    if opt == 3:
        os.system('cls' if os.name == 'nt' else 'clear')  # clearing screen
        sorted02 = []
       # making copy for sorting
        for i in range(0, len(merit)):
            sorted_merit.append(merit[i])
            sorted_merit[i] = float(sorted_merit[i])
        # top down sorting
        for i in range(0, len(merit)):
            largest = sorted_merit[0]
            largestidx = 0
            for j in range(0, len(merit)):
                if sorted_merit[j] > float(largest):
                    largest = sorted_merit[j]
                    largestidx = int(largestidx)
                    largestidx = j
            sorted_merit[largestidx] = -1
            sorted02.append(largestidx)

        counter = 0
        counter = int(counter)
        print("\t", "Name", "\t", "SSC", "\t",
              "FSc", "\t", "Ecat", "\t", "Aggregate")
        for i in range(0, len(merit)):
            counter = int(sorted02[i])
            print("\t", students[counter], "\t", matric[counter], "\t",
                  fsc[counter], "\t", ecat[counter], "\t", merit[counter])
        input("Press any key to continue...")

    if opt == 4:
        os.system('cls' if os.name == 'nt' else 'clear')  # clearing screen
        sorted03 = []
       # making copy for sorting
        for i in range(0, len(merit)):
            bottom_up.append(merit[i])
            bottom_up[i] = float(bottom_up[i])
        # bottom up sorting
        for i in range(0, len(merit)):
            smallest = bottom_up[0]
            smallestidx = 0                  # bubble sort
            for j in range(0, len(merit)):
                if bottom_up[j] < float(smallest):
                    smallest = bottom_up[j]
                    smallestidx = int(smallestidx)
                    smallestidx = j
            bottom_up[smallestidx] = 1000
            sorted03.append(smallestidx)

        counter_2 = 0
        counter_2 = int(counter_2)
        print("\t", "Name", "\t", "SSC", "\t",
              "FSc", "\t", "Ecat", "\t", "Aggregate")
        for i in range(0, len(merit)):
            counter_2 = int(sorted03[i])
            print("\t", students[counter_2], "\t", matric[counter_2], "\t",
                  fsc[counter_2], "\t", ecat[counter_2], "\t", merit[counter_2])
        input("Press any key to continue...")
