#12 42 23 96 7 18 10 133 add min and  max value
l=[12,42,23,96,7,18,10,133]
mini=l[0]
maxi=l[0]
for i in range(len(l)):
    if mini>l[i]:
        mini=l[i]
    if maxi<l[i]:
        maxi=l[i]
s=mini+maxi
d=mini-maxi
print(d)

    

