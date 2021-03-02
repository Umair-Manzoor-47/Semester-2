grams = 0
grams = input("Enter temperature in Celcius : ")

kg = int(grams) / 1000

if kg < 0:
    print("invalid")

else:
    print("temperature in F is : ", kg)
