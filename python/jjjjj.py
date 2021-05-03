matric = 0
first_year = 0
ecat = 0

#taking input 
matric = int(input("Enter matric marks :"))
first_year = int(input("Enter First year FSC marks :"))
ecat = int(input("Enter ecat marks :"))
hafiz = input("Is student hafiz?")

if haiz == 'yes' or hafiz == 'Yes':
    ecat = int(ecat) + 20

#claculating percentages
ecat_per = ecat*30 / 500
matric_per = matric*25 /1100
fsc_per = first_year*45 /520

#adding Percentages
merit = float(ecat_per) + float(matric_per) + float(fsc_per)
merit = float(merit)
#showig result
if merit > 0 and merit <= 100 :
    print("Your merit is :", merit)

else :
    print("Enteries are not valid...")

if merit >= 90 and merit <= 100:
    print("You're admitted in Electrical")

elif merit >= 85 and merit <= 89:
    print("You're admitted in Computer Engneering")

elif merit >= 83 and merit <= 84:
    print("You're admitted in Computer science")

elif merit >= 80 and merit <= 82:
    print("You're admitted in Mechanical Engneering")

elif merit >= 75 and merit <= 79:
    print("You're admitted in Architecture")
    