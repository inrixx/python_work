class Person():
	def __init__(self,name):
		self.name = name
		self.a = 800

	def hello(self):
		print('myange is ',self.name)



p = Person("bill")
p.hello()
print(p.name)
print(p.a)