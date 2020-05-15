#A function To check wether the dates are in leapyear or not

def  leapyear(year):
    if year%400==0:
        return True
    if year %100==0:
        return False
    if year % 4 ==0:
        return True
    return False
#function to check whether month is 31st or 30 28 or 29
def daysInmonth(year,month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month== 8 or month==10 or month ==12:
        
        return 31
    else:
        if month==2:
            if leapyear(year):
                return 29
            return 28
        else:
            return 30
# A function to return next day of the actual date      
def nextDay(year, month, day):
    if day < daysInmonth(year, month):
        return year, month, day+1
    else:
        if month < 12:
            return year, month+1, 1
        else:
            return year+1, 1, 1
# A function to check where the date one is before the date2 or not
def dateBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1==year2:
        if month1 < month2:
            return True
        if month1==month2:
            if day1 < day2:
                return True
    else:
        return False
# Finally to check the daybetweenDates
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days= 0
    
    while dateBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days+=1
        
    return days
    
  
    
    
    
    
def testDaysBetweenDates():
    
    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                              201, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30, 
                              2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30, 
                              2018, 1,  1)  == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 1, 1,
                              2013, 1, 1)  == 366)
    
    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")
    
testDaysBetweenDates()