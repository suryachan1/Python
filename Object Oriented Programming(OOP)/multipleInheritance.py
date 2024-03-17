#create a class of name placements which as fn info which displays we have 623 selects and stil counting
#create another class name dept which fn display which will display the naames of dept present in the college
#create a class pragati with a fn welcome which displays the mess welcome to pragati engineering college.
#and this pragati class should also display the detaills about departments and placeements

class placements:
    def info(self):
        print(' displays we have 623 selects and stil counting')
class dept:  #here also use placements sub class this is multilevel inheritance ex
    def display(self):
        print('cse')
        print('it')
        print('eee')
        print('ece')
        print('mech')
        print('civil')
        print('ai')
class pragati(placements,dept):
    def welcome(self):
        print('welcome to pragati engineering college')
obj=pragati()
obj.welcome()
obj.info()
obj.display()

        

