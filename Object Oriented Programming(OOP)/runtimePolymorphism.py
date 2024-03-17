#run time polymorphsm
#execution time polymorphism is also known as run time polymorphsm
#overriding is the concept of run time polymorphism--
#it occurs executing your program .it is possible in python

#method/function oveerriding
class father:
    def bike(self):
        print('harley devidson')
    def laptop(self):
        print('laptop with 2 gb and 500 gb hdd i5 process')

class surya(father):   #child class
    def laptop(self):   #method overriding
        print('as per my programming slw requarment the ')
        print('laptop with 8gb and 1000gb hdd i7 process')
obj=surya()
obj.bike()
obj.laptop()
    
#in python constructor and function overrinding is work

#constructor overriding   use super().__init__() in child class
