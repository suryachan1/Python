#in which you take an integer input from user if that integer if it is divisible by 3 and 6 print good no if the integer is divisible by 2 and 7 then print the avg no if the integer is divisible by 4 or 9 then print an aweson no else peint bad no
a=int(input('enter first no'))
if a%3==0 & a%6==0:
    print('good no')
elif a%2==0 & a%7==0:
    print('avg no')
elif a%4==0 | a%9==0:
    print('awesome no')
else:
    print('bad no')
