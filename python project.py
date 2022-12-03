
print("Enter the lowest year:")
date1=input("dd/mm/yyyy: ")
print("Enter the highest year:")
date2=input("dd/mm/yyyy: ")
year1=int(date1[6:])
year2=int(date2[6:])
leap_years=[]
non_leap_year=[]

if year1<year2:
    for i in range(year1,year2+1):
#Checking if the given year is a leap year
        if i%4==0 and i%100!=0:
            leap_years.append(i)
        
        if i%100==0 and i%400==0:
            leap_years.append(i)
            i=i+1
    print("Leap years in the given range",year1,"and", year2,"are:")
    print(leap_years)
else:
    print("Check your year inputs again:")
if year1<year2:
    for i in range(year1,year2+1):
#Checking if the year is not a leap year
        if i%4!=0:
            non_leap_year.append(i)
        
        if i %4==0 and i % 100==0:
            if  i%100==0 and i % 400!=0:
                non_leap_year.append(i)
    print("Non leap years in the given range",year1,"and",year2,"are:")
            
    print(non_leap_year)
else:
    print("Check your year input again :")