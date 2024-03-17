#filehandling
#f=open(filename,mode) #after use file.close()
#binary files use last in b --ex 'rb'
# import csv  from append use any .csv file use csv.writer(varname),, ---use rows varname.writerow([]) listvar taking var an input from user in columns
'''---------modes-----------
r=read only for existing file no changes  --1)file.read() or also use number how many char will be return(use for call)
w=write operation,file is no, to create a new file in w ,already file data is override existing data. so present only existing data--1)file.write()(use for call) 2)file.writelines()
a=append operation same as w but not override the data.--1)file.write(use for call)
r+=to read and write,
w+=write as well as read
a+=append and readtogether'''



#operation with csv file (for create new file)
import csv
f=open('student.csv','a',newline='')
a=csv.writer(f)   #csv.dictReader for r operation
a.writerow(['studentid','rollno','name'])
studentid=int(input('enter studentid'))
rollno=int(input('enter rollno'))
name=input('enter name')
a.writerow([studentid,rollno,name])
print('student record has save')


