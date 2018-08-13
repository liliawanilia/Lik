from datetime import date
from datetime import timedelta

day = date.today()

if day.weekday () == 5:
       workingday = day + timedelta(days = 2)
elif day.weekday() == 6:
       workingday = day + time.delta(days = 1)
else:
       workingday = day

print('working day is' ,workingday)
