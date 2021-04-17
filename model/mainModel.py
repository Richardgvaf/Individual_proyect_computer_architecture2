from model.singletonView import *
class mainModel():
	i = 12345
	def f(self):
		s1 = Singleton()
		s2 = Singleton()
		if id(s1) == id(s2):
		    print("Singleton works, both variables contain the same instance.")
		else:
		    print("Singleton failed, variables contain different instances.")
		
		s1.some_business_logic()
		return 'hello world Test'

