#to check the type of triangle where you take input from user for 3 sides and classify it accordingly equlateral,iso and scaler
a=int(input('enter side1'))
b=int(input('enter side2'))
c=int(input('enter side3'))
if a==b==c:
    print('equlateral')
elif (a==c) or (b==c) or (c==a):
    print('iso')
elif a!=b!=c:
    print('scaler')
else:
    print('valid answers')
