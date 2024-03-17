#self is used to access the var throughtout the class
class faculty:  #parent class
    def __init__(self,f_name,dpartment,f_id):
        self.f_name=f_name
        self.dpartment=dpartment
        self.f_id=f_id
    def print_info(self):
        print('faculty information',self.f_name,self.dpartment,self.f_id)
obj= faculty('surya','it',1255)
obj.print_info()

class cse(faculty):  #child class
    pass             #no statement
obj=cse('chandra','cse',12555)
obj.print_info()
