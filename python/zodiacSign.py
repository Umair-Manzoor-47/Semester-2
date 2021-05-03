# taking input
days = int(input("Enter your Birthday : "))
month = int(input("Enter your Birth month : "))

#compairing
if(((days >= 22) and (month == 12)) or ((days <= 20) and (month == 1))):
    print("capricon")
if(((days >= 21) and (month == 1)) or ((days <= 19) and (month == 2))):
    print("aquarius")
if(((days >= 20) and (month == 2)) or ((days <= 20) and (month == 3))):
    print("pisces")
if(((days >= 21) and (month == 3)) or ((days <= 20) and (month == 4))):
    print("aries")
if(((days >= 20) and (month == 4)) or ((days <= 20) and (month == 5))):
    print("taurus")
if(((days >= 23) and (month == 5)) or ((days <= 21) and (month == 6))):
    print("gemini")
if(((days >= 22) and (month == 6)) or ((days <= 23) and (month == 7))):
    print("cancer")
if(((days >= 24) and (month == 7)) or ((days <= 23) and (month == 8))):
    print("leo")
if(((days >= 24) and (month == 8)) or ((days <= 22) and (month == 9))):
    print("virgo")
if(((days >= 23) and (month == 9)) or ((days <= 22) and (month == 10))):
    print("libra")
if(((days >= 23) and (month == 10)) or ((days <= 22) and (month == 11))):
    print("scorpio")
if(((days >= 23) and (month == 11)) or ((days <= 20) and (month == 12))):
    print("sagitanus")
