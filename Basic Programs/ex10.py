#fabonacci series
#  a b c
#a b c 
#0 1 1 2 3 5 8 13 21 34
a=0
b=1
print(a)
print(b)

for i in range(1,9):
    c=a+b
    print(c)
    a=b       #a,b=b,c
    b=c
