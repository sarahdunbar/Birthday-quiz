"""
birthday.py
Author: Sarah Dunbar
Credit: none
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
todaydate = datetime.today().day


name = input ("Hello, what is your name? ")
month = input ("Hi " + name + ", what was the name of the month you were born in? ")
year = input ("And what year were you born in, " + name + "? ")
date = input ("And the day? ")
if month == "October" or month == "october":  
    if date == "31":
        print ("You were born on Halloween!")
if month ==  tdmonth:
    print ("Oh, so close!")
    if date == todaydate:
        print ("Happy birthday!")


