#constructors using parameters
class f15:
    def __init__(self,a,b):
        print('the no of placements is 650 and still counting')
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

surya=f15(10,20)
surya.light('white')
surya.fan(56)
surya.ac(16,35)
surya.displays()

