class Animal(object):
	def sound(self):
		print('animal sounds')

class Dog(Animal):
	_classId = 1000

	def getClassId(self):
		return Dog._classId

	def __init__(self, name = 'unkonw', age = 'unkonw'):
		self.m_name = name
		self.m_age = age

	def __str__(self):
		return 'class Dog, name: {}, age: {}'.format(self.m_name, self.m_age)

	def getName(self):
		return self.m_name

	def getAge(self):
		return self.m_age

	def selfIntroduction(self):
		print(f'dog:{self.m_name}	age:{self.m_age}	sound:wang wang wang')

	def sound(self):
		print('god sounds')



class Cat(Animal):
	_classId = 10001

	def getClassId(self):
		return Cat._classId

	def __init__(self, name='unkonw', age='unkonw'):
		self.m_name = name
		self.m_age = age
	
	def __len__(self):
		return 1

	def getAge(self):
		return self.m_age

	def getName(self):
		return self.m_name

	def selfIntroduction(self):
		print(f'cat:{self.m_name}	age:{self.m_age}	sound:miao miao miao')

	def sound(self):
		print('cat sounds')

def main():
	a = Animal()
	d1 = Dog()
	d2 = Dog('dd', 1)
	c1 = Cat()
	c2 = Cat('cc', 2)

	a.sound()

	d1.selfIntroduction()
	d2.selfIntroduction()
	c1.selfIntroduction()
	c2.selfIntroduction()

	print(d1.getClassId(), d2.getClassId())
	print(c1.getClassId(), c2.getClassId())

	d1.sound()
	c1.sound()

	print(d1)
	print(c1)

	print(len(c1))

if __name__ == '__main__':
	main()