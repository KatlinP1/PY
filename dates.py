from datetime import date
date1= date(2014, 7, 2)
date2= date(2014, 7, 11)
x= date2-date1
print (x)

def datediff(d1,d2):
    return d2-d1

y = datediff(date(2019, 1, 1), date(2019,8,7))
print (y)
