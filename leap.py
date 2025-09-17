def leap_year(year):
    total= (year % 4 == 0 and year % 100 != 0 or year %100 ==0 and year%400==0 ) 
    return total
