val = 0
current_unit = 0
unit_convert = 0
result = 0

# input
val = float(input("Enter value for conversion :"))
current_unit = input("Enter unit of current value :")
unit_convert = input("Enter desired unit :")

# performing calculation
if unit_convert == 'kg' and current_unit == 'g':
    result = val / 1000

if unit_convert == 'g' and current_unit == 'kg':
    result = val * 1000

if unit_convert == 'usd' and current_unit == 'pkr':
    result = val / 162

if unit_convert == 'hours' and current_unit == 's':
    result = val / 3600

if unit_convert == 'cm' and current_unit == 'm':
    result = val * 100

print("Your converted value is :", result, unit_convert)
