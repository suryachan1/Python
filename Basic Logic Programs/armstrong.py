#armstrong no 153=1^3+5^3+3^3=153    nod  sod power digit extract
'''n=int(input('enter no'))
#mod=0
n1=n
while(n>0):
    nod=nod+1
    n=n//10
sod=0
digit=n1
while(n1>0):
    digit=n1%10
    sod=sod+digit**mod
    n1=n1//10
if(sod==org):
   print('yes')
    '''
def check_armstrong(num):
    if num == 0:
        return num
    else:
        return pow((num%10),order) + check_armstrong(num//10)

num = int(input("Enter a number to check if it is an Armstrong number or not: "))

order = len(str(num))  
sum = check_armstrong(num)

if sum == int(num):
    print(num,"is an Armstrong Number.")    
else:
    print(num,"is not an Armstrong Number.")
