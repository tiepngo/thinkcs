import calendar
cal = calendar.TextCalendar(firstweekday=3)      # Create an instance
cal.pryear(2020)                   # What happens here?
cal.prmonth(2020,3)

d = calendar.LocaleTextCalendar(6, "VIETNAMESE")
d.pryear(2012)

print(calendar.isleap(2020))