file=open('surya.txt','w')
file.write('my name is surya')
file.write('surya surya')
file.close()


#second method

with open('surya.txt','w') as file:
    file.write('my name is surya')
