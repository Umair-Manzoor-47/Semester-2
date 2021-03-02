day = 0 
age = 0
#Taking input
age = int(input("Enter Age = "))
day = int(input("Enter Day of Week 1-7 :"))
 

if (day==1) :       
       print("The museum is closed.")
    
if((day == 2) or (day == 4)):
        print("You get half price discount!")
    
if(((age>=13) and (age<=20)) and (day == 3)) :
        print("You get half price discount!")

else :
        print("You pay full price.")
 