from datetime import datetime, timedelta

today = datetime.now()
print("Today is: " + str(today))
print("Day: " + str(today.day))
print("Month: " + str(today.month))
print("Year: " + str(today.year))
print("Hour: " + str(today.hour))
print("Minute: " + str(today.minute))
print("Second: " + str(today.second))

# timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
print("Yesterday was: " + str(yesterday))
one_week = timedelta(weeks=1)
week_ago = today - one_week
print("Week ago was: " + str(week_ago))

birthday = "01/04/1980"
birth_date = datetime.strptime(birthday, "%d/%m/%Y")
print("Birthday is " + str(birth_date))
bday_eve = birth_date - one_day
print("Birthday eve is " + str(bday_eve))
