l=[5,8,'sai',76 ,'aaa'] #create     
print(type(l))
len(l)

print(l[0]) #accessing
print(l[3])

print(l[:3:2]) #slicing
print(l[::-1])

for i in l:  #looping
    print(i)
    
    
l.append('surya') #end

l.insert(1,'aaa') #specified location
print(l)

l.remove('sai')  #remove

a=[2,4,'sdah',l]  #nested list
print(a)

a[0]='surya'     #update
print(a)


c=[[4,6],['sai','sui']]  #multidimensional
print(c[0])
print(c[0][1])

