a='1234'
b=0
d=0
e=1000
h=5
print('Welcome To ATM')
while b<5:
    c=input('\nEnter Your Pin\n')
    if c==a:
        print('\nAcces Granted')
        while d!=4:
            print('\n*** MENU ***\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit')
            d=int(input('\nEnter your Choice:'))
            if d==1:
                print('Your Balance is:',e)
            elif d==2:
                f=int(input('\nEnter Your Amount'))
                e=e+f
                print('Your Balance is:',e)
                print('Deposited Succesfully')
            elif d==3:
                g=int(input('\nEnter a amount:'))
                if g<=e:
                    e=e-g
                    print('Your Balance is:',e)
                    print('Withdraw succesfully')
                else:
                    print('Please Enter Valid Amount')
            elif d>6:
                print('Invalid Choice')
        print('\nThanku Vist Again')
        break
    else:
        b=b+1
        print('\nIncorrect pin\nAttmepts Left:',h-b)
    continue
print('\nAccess Closed!')
