#constructors in class =is a fn as soon as execute automatically (cons is one which allocate the memory)
'''#create a class f15 with functions lights is called its prints out the color of the 1 light, which is taken as parameter to the fn
#2fan when fan fn is call it displays the regulator speed in which rotating,displays the parameter of a fn
#3 ac displays the room temp and the outside temp which are taken as parameter
#4fn name is display which displays to diif in outside temp and room temp of ac and also the fan speed '''
class f15:
    def __init__(self):
        print('the no of placements is 650 and still counting')
        a=10
        b=20
        print(a*b)
    def light(self,color):
        print(color)
    def fan(self,speed):
        self.sp=speed
        print(speed)
    def ac(self,rtemp,otemp):
        self.ote=otemp
        self.rte=rtemp
        print(rtemp,otemp)
    def displays(self):
        print(self)
        diff=self.ote-self.rte
        print(diff)
        print(self.sp)

surya=f15()
surya.light('white')
surya.fan(56)
surya.ac(16,35)
surya.displays()



