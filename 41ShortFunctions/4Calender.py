# import  calendar
#
# print(calendar.TextCalendar(firstweekday=6).formatyear(2020))


# Python program to Find day of
# the week for a given date
import datetime
import calendar


def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])


# Driver program
date = '18 08 2020'
print(findDay(date))