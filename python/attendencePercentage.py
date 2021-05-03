total_classes = 0
attended_classes = 0

total_classes = int(input("Enter total classes held:"))
attended_classes = int(input("Enter classes you attended:"))

percentage = int((attended_classes/total_classes) * 100)

if percentage <= 100 and percentage >= 0:
    if percentage >= 75:
        print("your attendance % is", percentage)
        print("You allowed for exams")
    else:
        print("your attendance % is", percentage,
              "your attandance is less than 75%.")
        print("You're not allowed to sit in exams I'm afraid.")

else:
    print("Enter valid commands...")
