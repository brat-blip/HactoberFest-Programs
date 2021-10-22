month = input("What is the current month?: ")
date = int(input("What is the current day?: "))
day = input("What is the current day of the week?: ")
extra = int(input("How many days in the future do you want to calculate?: "))

days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
month_to_number = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
number_to_month = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
days_to_number = {"Sunday":1, "Monday":2, "Tuesday":3, "Wednesday":4, "Thursday":5, "Friday":6, "Saturday":7}
number_to_days = {1:"Sunday", 2:"Monday", 3:"Tuesday", 4:"Wednesday", 5:"Thursday", 6:"Friday", 7:"Saturday"}

day_of_year, new_month, new_date, new_day = None, None, None, None
new_day = days_to_number[day]+extra
new_day%=7
new_day = number_to_days[new_day]

days_left_that_year = -date
for i in range(month_to_number[month],13):
   days_left_that_year+=days[i]

if extra<=days_left_that_year:
   day_of_year = 0
   for i in range(1,month_to_number[month]):
       day_of_year+=days[i]
      
   if extra+date<=days[month_to_number[month]]:
       new_month = month
       new_date = extra+date
       day_of_year+=(extra+date)
   else:
       day_of_year+=extra+date
      
       extra-=(days[month_to_number[month]]-date)
       new_month = month_to_number[month]+1
       while extra>days[new_month]:
           extra-=days[new_month]
           new_month+=1
      
       new_month = number_to_month[new_month]
       new_date = extra
else:
   extra-=days_left_that_year
   extra%=365
  
   day_of_year=extra
   new_month=1
   while extra>days[new_month]:
       extra-=days[new_month]
       new_month+=1
  
   new_month = number_to_month[new_month]
   new_date = extra
  
print("That will be the",day_of_year,end=" ")
if day_of_year%10==1:
   print("st",end=" ")
elif day_of_year%10==2:
   print("nd",end=" ")
elif day_of_year%10==3:
   print("rd",end=" ")
else:
   print("th",end=" ")
print("day of the year")

print("That day will be:",new_month,new_date)

print("It will be a",new_day)
