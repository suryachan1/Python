n=int(input('enter 5no '))
rev=0
while(n>0):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print('the rev no:',rev)



'''
n=12345
while(n>0):
digit=n%10
print(digit)
n=n//10
