#write a recursive fn to count the number of digits of a no
def count(n):
    if n==0:
        return 0
    return 1+count(n//10)
print(count(123))
