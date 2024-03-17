#checking if the year is leaf year or not
#year is div by 4 and not div by 100 or if it is div by 400 then it is call the leaf year
year=int(input('enter the year'))
if year%4==0 and year%100!=0 or y%400==0:
    print('if the year is leap year')
else:
    print('if the year is not leap year')

        
    
