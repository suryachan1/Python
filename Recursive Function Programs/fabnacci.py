#f(n)=f(n-1)+f(n-2)
def fab(n):
    if n<=1:
        return n
    else:
        return(fab(n-1)+fab(n-2))
nterms=10
for i in range(nterms):
    print(fab(i))
