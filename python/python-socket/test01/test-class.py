class Parent:
    '''parent class'''
    parentAttr = 100
    def __init__(self):
        print 'parent init'

    def set(self, attr):
        self.parentAttr = attr

    def get(self):
        print self.parentAttr


class Child(Parent):

    def __init__(self):
        print 'child init'

    def set(self, attr):
        self.parentAttr = attr+1

a1 = Parent()

a1.set(10)
a1.get()    #11

b1 = Child()

b1.set(10) 
b1.get()    #11

