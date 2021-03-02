books = 0
price = 0

books = int(input("Enter number of books you purchased :"))
price = books * 100

if price > 1000:
    bonus = int(price)/10
    print("Your got 10% bnus on your purchase which is",
          bonus, "you have to pay:", price - int(bonus))

else :
    print(" You have to pay :", price)
