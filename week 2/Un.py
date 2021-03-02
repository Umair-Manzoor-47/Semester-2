"""
def read_data(dataTocheck, postion):
    idx = 0
    spaceFound = 0
    name = ""
    while idx < len(dataTocheck):
        c = dataTocheck[idx]
        if c == ' ':
           spaceFound += 1

        elif (spaceFound == postion):
           name = name + c

        idx += 1
    return name


myfile = open("data.txt", "r")
records = myfile.read().splitlines()
for i in records:
    id = read_data(i, 0)
    pin = read_data(i, 1)

# def validation(email):
email = input("Enter : ")
is_true = True
length = len(email)
idx = 0
if email[length-1] != "m":
    is_true = False

if email[length-2] != "o":
    is_true = False

if email[length-3] != "c":
    is_true = False

if email[length-4] != ".":
    is_true = False

while idx < length:
    if email[idx] == "@":
        is_true = True

    idx += 1

if is_true == True:
    print("True")
else :
    print("false")
"""
def password_validator(enter_password):
    enter_password = input("Enter: ")
    flag = False

    length = len(enter_password)

    if length >= 8:
        for i in range(length):
            if enter_password[i] >= 'A' and enter_password[i] <= 'Z':
                flag = True
                break
        if flag == True:
            for j in range(length):
                """if ((enter_password[j] >= 33 and enter_password[j] <= 47) or (enter_password[j] >= 58 and enter_password[j] <= 64) or (enter_password[j] >= 91 and enter_password[j] <= 96) or (enter_password[j] >= 123 and enter_password[j] <= 126)):"""
                if enter_password[j] >= "a" and enter_password[j] <= "z": 
                    flag = True
                    break
                else:
                    flag = False
        if flag == True:
            for k in range(length):
                if enter_password[k] == "#" or enter_password[k] == "&" or enter_password[k] == "$": 
                    flag = True
                    break
                else:
                    flag = False
        if flag == True:
            for l in range(length):
                if enter_password[l] >= "0" and enter_password[l] <= "9": 
                    flag = True
                    break
                else:
                    flag = False

    if flag == True :
        print("Password is true")
    else :
        print("Password is not correct")