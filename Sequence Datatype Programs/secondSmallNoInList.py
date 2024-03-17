#to find the second smallest negative no from the list
l=[22,-1,42,65,1,-4,6]
'''m1=999
m2=999
for i in range(len(l)):
    if l[i]<m1:
         m1=l[i]
    if l[i]<m2 and l[i]!=m1:
         m2=l[i]
         print(m2)



'''




m1=999
m2=999
for i in range(len(l)):
    if l[i]<m1:
        m2=m1
        m1=l[i]
    else:
        m2>l[i] and m2>m1
        m2=l[i]
print(m1)
    


