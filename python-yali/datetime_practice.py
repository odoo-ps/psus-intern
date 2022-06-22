#datetime is a module allowing to work with dates and times
from datetime import datetime
#to get current date and time, to get only time-->.time()
date_object=datetime.now()
print(date_object)

#extract day,month, year by strftime(arg), 1.convert time to string 
# 2.arg would be "%d" for day
#"%m" for month, "%Y" for year
day=date_object.strftime("%d")
print(day)
year=date_object.strftime("%Y")
print(year)
month=date_object.strftime("%m")
print(month)
#strptime(arg1, arg2) function-->string to date,return datetime object.
#arg1:string(to be converted into datetime) arg2:format code
date_string='20 April,1997'
new_date_object=datetime.strptime(date_string,'%d %B,%Y').date()
print(f"the date object:{new_date_object}")

#exercises
'''
Write a Python script to display the various Date Time formats.
a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week
'''
current_date_and_time=datetime.now()
current_year=current_date_and_time.strftime('%Y')
month_of_year=current_date_and_time.strftime('%m')#"%B" for english expression
week_number_of_year=current_date_and_time.strftime('%W')
day_of_year=current_date_and_time.strftime("%j")
day_of_month=current_date_and_time.strftime("%d")
day_of_week=current_date_and_time.strftime("%A")
print(f"current date and time:{current_date_and_time}")
print(f"current year:{current_year}")
print(f'the month of year:{month_of_year}')
print(f'week number of year:{week_number_of_year}')
print(f'day of year:{day_of_year}')
print(f'day of month:{day_of_month}')
print(f'day of week:{day_of_week}')

