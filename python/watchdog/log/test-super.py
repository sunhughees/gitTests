# -*- coding: utf-8 -*-

# class FooParent(object):
# 	'''Hi'''

# 	def bar(self, message):
# 		print(message)

# class FooChild(FooParent):
# 	def bar(self, message):
# 		# FooParent.bar(self, message)
# 		super(FooChild, self).bar(message)


# oneInstance = FooChild()

# oneInstance.bar("Hello, World!")

#--------------------------------------

class B(object):
	def __init__(self):
		pass

	def meth(self, arg):
		print arg


class C(B):

    def __init__(self):
        pass

    # def meth(self, arg):
    #     pass

    def meth(self, arg):
        super(C, self).meth(arg)



a = C()

a.meth("Hi")


#--------------------------------------

# class FooParent(object):  
#     def __init__(self):  
#         self.parent = 'I\'m the parent.'  
#         print 'Parent'  
      
#     def bar(self,message):  
#         print message,'from Parent'  
  
# class FooChild(FooParent):  
#     def __init__(self):  
#         super(FooChild,self).__init__()  
#         print 'Child'  
          
#     def bar(self,message):  
#         super(FooChild, self).bar(message)  
#         print 'Child bar fuction'  
#         print self.parent  
  
# if __name__ == '__main__':  
#     fooChild = FooChild()  
#     fooChild.bar('HelloWorld')  
