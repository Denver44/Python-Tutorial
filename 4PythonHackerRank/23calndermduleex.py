import  datetime
import calendar

date = input()

day = datetime.datetime.strptime(date, '%m %d %Y').weekday()
print(calendar.day_name[day].upper())