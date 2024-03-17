#write a recursive fn to calculate the sum of digits of a no
def count(n):
    if n==0:
        return 0
    return n%10+count(n//10)
print(count(12345))
