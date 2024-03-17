#read mode first your txt file present in your device
file=open('surya.txt','r')
print(file.read())


#using for loop

file=open('surya.txt','r')
for a in file:
    print(a)

