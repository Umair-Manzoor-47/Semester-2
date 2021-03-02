matric = 0
first_year = 0
ecat = 0

#taking input 
matric = int(input("Enter matric marks :"))
first_year = int(input("Enter First year FSC marks :"))
ecat = int(input("Enter ecat marks :"))

#claculating percentages
ecat_per = ecat*30 / 400
matric_per = matric*25 /1100
fsc_per = first_year*45 /520

#adding Percentages
merit = float(ecat_per) + float(matric_per) + float(fsc_per)

#showig result
if merit > 0 and merit <= 100 :
    print("Your merit is :", merit)

else :
    print("Enteries are not valid...")