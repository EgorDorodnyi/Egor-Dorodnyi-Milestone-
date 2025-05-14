#this is my saving calulator, it tells you how much weeks you need to work to buy your things
#I am asking thier hours and how much thier goal costs
Hours_per_week = int(input("How much hours do you work a week?:"))
Hourly_pay = float(input("how much are you paid per hour?: "))
Goal = input("What do you want to buy? ")
Goal_price = float(input("how much does it cost?:"))

#Calcuates and also automatcly rounds it

Weekly_earnings = Hourly_pay * Hours_per_week
Time_needed = Goal_price / Weekly_earnings

Time_needed = round(Time_needed)

#I am now showing how much hours they need to work for thier item

print("You need to work {} weeks to afford a {}".format(Time_needed, Goal))