#method overloading is known as compile time polymorphism
#using the same name but diff funcationality is called overloading
#using the same name same funcationality but diff parameters is known as method/function (overloading python not support method overloadig)
class arith:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
obj=arith()
obj.add(10)
obj.add(13,12)
obj.add(23,34,23)              #latest fn will be consider as fn remaining all are not consider(so not working)

#method overloading is known as compile time polymorphism        
#in python only operator overloading is work but constructor ,method are not workSS
