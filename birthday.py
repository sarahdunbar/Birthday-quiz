"""
birthday.py
Author: Sarah Dunbar
Credit: Mr. Dennison
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""

import datetime
from datetime import datetime
import calendar
from calendar import month_name
todaymonth = datetime.today().month
tdmonth = month_name[todaymonth]
tddate = datetime.today().day
todaydate = str(tddate)

name = input ("Hello, what is your name? ")
month = input ("Hi " + name + ", what was the name of the month you were born in? ")
yr = input ("And what year were you born in, " + name + "? ")
year = int(yr)
date = input ("And the day? ")
if month == "October" or month == tdmonth:
    if month == "October":  
        if date == "31":
            print ("You were born on Halloween!")
    if month ==  tdmonth:
        if date == todaydate:
            print ("Happy birthday!")
else:
    if month == "December" or month == "January" or month == "February":
        season = " winter "
    if month == "March" or month == "April" or month == "May":
        season = " spring "
    if month == "June" or month == "July" or month == "August":
        season = " summer "
    if month == "September" or month == "November":
        season = " fall "
    if year >= 2000:
        age = " two thousands."
    if year >= 1990 and year <= 1999:
        age = " nineties."
    if year >= 1980 and year <= 1989:
        age = " eighties."
    if year <= 1979:
        age = " stone age."
    print (name + ", you are a" + season + "baby of the" + age)




