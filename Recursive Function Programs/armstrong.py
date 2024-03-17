#armstong using recursion(not executed)
def cod(n):
    if n==0:
        return 0
    return 1+cod(n//10)
count=cod(153)
def arm(n,c):
    if n==0:
        return 0
    return n%10**c+arm(n//10,c)
n=int(input())
count_value=count(n)
if n==cod(n):
    print('armstrong no')
