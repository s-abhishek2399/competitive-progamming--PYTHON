
import calendar
x,y,z=map(int,input().split())
c=calendar.day_name[calendar.weekday(z,x,y)]
print(c.upper())
