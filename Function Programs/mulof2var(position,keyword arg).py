#a fn which takes 2 paramaters/arguments a and b type cast the value of second argument into int then multiply both the arguments and print the last digit of a result
def name(a,b):  #a=4,b=5 defaut arguments
    b=int(b)
    c=a*b
    print(c%10)
name(11,12.3)#position argument
#a=12,b=12.3  keyword arguments
