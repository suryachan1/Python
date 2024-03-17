class base:
    def __init__(self):
        print('parent class constructor')
        self.__a=2
        print(self.__a)
class derived(base):
    def __init__(self):
        base.__init__(self)
        print('calling')
        #print(self.__a)
#obj1=derived()
#print(obj1.__a)
obj2=base()
Sprint(obj2.__a)
