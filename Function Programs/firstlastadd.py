#fn to calculate sum of first and last digit of a no, no should be taken as a arg 785=12
sum=0
def cal(a):
    c=a%10       #lastdigit extraction
    while(a>10): #firstdigit extraction
        a=a//10
    b=a%10
    sum=b+c
    print(sum)
cal(785)
    
    
