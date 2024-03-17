#encapulation :dividing data into diff groups making that whole data in one unit[dividing into 3 types there are called as access specifier
#public     :global  var all class are use
#protected(_a):one class and derived classes are used
#private(__a) :only access in one class

'''unfortunately,in python protected,private and that much that procted'''

class base:
    def __init__(self):
        print('parent class constructor')
        self._a=2
class derived(base):
    def __init__(self):
        base.__init__(self)
        print('calling')
        print(self._a)
obj1=derived()
print(obj1._a)
obj2=base()
print(obj2._a)
