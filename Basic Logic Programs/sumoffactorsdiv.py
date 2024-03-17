#take no from user check if the sum of factors of that no is > than the original no or not
a=int(input('enter the no'))
sum=0
for i in range(1,a):
    if(a%i==0):
        sum=sum+i
if(sum>a):
    print('abundant')  #a<sum
else:
    print('no')
