service = 0
salary = 0
bonus = 0

service = int(input("Enter your service span :"))
salary = int(input("Enter your salary : "))

if service >= 5:
    bonus = salary/20
    print("You got 5% bonus which is", int(bonus),
          "your salary is : ", salary + (bonus))

else:
    print("Sorry! you got no 'Bonus' your salary is :", salary)