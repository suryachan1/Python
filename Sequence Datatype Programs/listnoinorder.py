l=[2,0,1024,0,40,230,0]
a=[]  #extra list
for i in range(len(l)):
    if l[i]!=0:
        a.append(l[i])

for i in range(len(l)):
        
    if l[i]==0:
        a.append(l[i])
print(a)
