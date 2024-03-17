#palindrom 1221 1221 check

n=int(input('enter the no'))
rev=0
n1=n
while(n>0):
    digit=n%10
    rev=rev*10+digit 
    n=n//10
if(rev==n1):
    print('yes palindrom')
else:
    print('no palindrom')
