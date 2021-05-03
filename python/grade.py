score = 0

#input
score = int(input("Enter Marks :"))

#checking for input
if score >= 0 and score <= 100 :
    if score < 25 :
        print("your grade is F.")
    if score > 25 and score <= 45 :
        print("your grade is E.")
    if score <= 50 and score > 45 :
        print("your grade is D.")
    if score > 50 and score <= 60 :
        print("your grade is C.")
    if score > 60 and score <= 80 :
        print("your grade is B.")
    if score > 80  :
        print("your grade is A.")
                
else :
    print("Enter valid numbers")