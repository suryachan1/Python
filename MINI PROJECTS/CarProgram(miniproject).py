#three car companies toyota mahindra and merceds.
'''#take the input from user for the car company name and in the inpue mess give the user in the 3 of the companies this user input company name goes as the
   input/argument to model name fn ,which welcomes the user accordingly to the company name.'''
#the first fn itself,ask the user to enter the specific model name for that company.
#the second fn whose name is varient according to the car company name and car model the user should be ask to enter the varient he would like to choose from petrol,desiel
'''#the last dissplay fn according to the car company ,car model name and car varient first its ex shooroom price will be displayed and then its onroad price should be displayed,
    which is cal as ex showroom price +cgst+sgst+insurance.the sgst cgst and the insurance all three have a common value throught the car showroom'''
def onroadprice(n):
    print('\nThe showroom price of the car is : ',n)
    cgst=n*10/100
    sgst=n*10/100
    insurance=n*15/100
    total=n+cgst+sgst+insurance
    print('The total price of the car includes :\nCGST(10%)=',cgst,'\nSGST(10%)=',sgst,'\nINSURANCE(15%)=',insurance,'\nTOTAL PRICE = ',total)
    print()
    carshowroom()

def carshowroom():
    while(True):
        n=int(input('Please Select a option of car company names given below:\n1.TATA\n2.MAHINDRA\n3.TOYOTA\n4.Exit\n'))
        if n==1:
            print('WELCOME TO TATA CARS FAMILY!')
            while(True):
                m=int(input('Enter a option for the TATA CAR MODELS given below:\n1.Nano\n2.Altroz\n3.Harrier\n4.Back\n'))
                if m==1:
                    while(True):
                        v=int(input('enter a option of variant of the TATA NANO cars given below:\n1.Petrol\n2.Diseal\n3.Back\n'))
                        if v==1:
                            onroadprice(100000)
                            break
                        elif v==2:
                            onroadprice(150000)
                            break
                        elif v==3:
                            break
                        else:
                            print('Invalid option!\n')
                elif m==2:
                    while(True):
                        v=int(input('enter a option of variant of the TATA ALTROZ cars given below:\n1.Petrol\n2.Diseal\n3.Back\n'))
                        if v==1:
                            onroadprice(500000)
                            break
                        elif v==2:
                            onroadprice(550000)
                            break
                        elif v==3:
                            break
                        else:
                            print('Invalid option!\n')
                elif m==3:
                    while(True):
                        v=int(input('enter a option of variant of the TATA HARRIER cars given below:\n1.Petrol\n2.Diseal\n3.Back\n'))
                        if v==1:
                            onroadprice(2000000)
                            break
                        elif v==2:
                            onroadprice(2050000)
                            break
                        elif v==3:
                            break
                        else:
                            print('Invalid option!\n')
                elif m==4:
                    break

                else:
                    print('Enter the valid option\n')

      
        elif n==2:
            print('WELCOME TO MAHINDRA CARS FAMILY!')
            while(True):
                m=int(input('Enter a option for the MAHINDRA CAR MODELS given below:\n1.XUV700\n2.BOLERO\n3.SCORPION\n4.Back\n'))
                if m==1:
                    while(True):
                        v=int(input('enter a option of variant of the XUV700 cars given below:\n1.Petrol\n2.Diseal\n3.Back\n'))
                        if v==1:
                            onroadprice(100000)
                            break
                        elif v==2:
                            onroadprice(150000)
                            break
                        elif v==3:
                            break
                        else:
                            print('Invalid option!\n')
                elif m==2:
                    while(True):
                        v=int(input('enter a option of variant of the BOLERO cars given below:\n1.Petrol\n2.Diseal\n3.Back\n'))
                        if v==1:
                            onroadprice(500000)
                            break
                        elif v==2:
                            onroadprice(550000)
                            break
                        elif v==3:
                            break
                        else:
                            print('Invalid option!\n')
                elif m==3:
                    while(True):
                        v=int(input('enter a option of variant of the SCORPION cars given below:\n1.Petrol\n2.Diseal\n3.Back\n'))
                        if v==1:
                            onroadprice(2000000)
                            break
                        elif v==2:
                            onroadprice(2050000)
                            break
                        elif v==3:
                            break
                        else:
                            print('Invalid option!\n')
                elif m==4:
                    break

                else:
                    print('Enter the valid option\n')

        

        elif n==3:
            print('\nWELCOME TO TOYOTA CARS FAMILY!')
            while(True):
                m=int(input('Enter a option for the TOYOTA CAR MODELS given below:\n1.URBAN\n2.ETHIOUS\n3.FORTUNER\n4.Back\n'))
                if m==1:
                    while(True):
                        v=int(input('enter a option of variant of the URBAN cars given below:\n1.Petrol\n2.Diseal\n3.Back\n'))
                        if v==1:
                            onroadprice(100000)
                            break
                        elif v==2:
                            onroadprice(150000)
                            break
                        elif v==3:
                            break
                        else:
                            print('Invalid option!\n')
                elif m==2:
                    while(True):
                        v=int(input('enter a option of variant of the ETHIOUS cars given below:\n1.Petrol\n2.Diseal\n3.Back\n'))
                        if v==1:
                            onroadprice(500000)
                            break
                        elif v==2:
                            onroadprice(550000)
                            break
                        elif v==3:
                            break
                        else:
                            print('Invalid option!\n')
                elif m==3:
                    while(True):
                        v=int(input('enter a option of variant of the FORTUNER cars given below:\n1.Petrol\n2.Diseal\n3.Back\n'))
                        if v==1:
                            onroadprice(2000000)
                            break
                        elif v==2:
                            onroadprice(2050000)
                            break
                        elif v==3:
                            break
                        else:
                            print('Invalid option!\n')
                elif m==4:
                    break

                else:
                    print('Enter the valid option\n')
        

        elif n==4:
            print('\nTHANKS FOR VISITING OUR SHOWROOM ')
            quit()
        
        if n not in(1,2,3,4):
            print('INVALID OPTION\n')


print('#Welcome to AASS Car show room#\n')
carshowroom()
    
