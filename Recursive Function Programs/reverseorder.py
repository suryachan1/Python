#digits print in reverse order
def reverse(n):
    if n==0:
        return 0
    else:
        mod=(n%10)
        print(mod)
        return reverse(n//10)
n=int(input())
reverse(n)

 '''def reverse(n):
    if n==0:
        return
    print(n%10)
    return reverse(n//10)
reverse(12345)'''
