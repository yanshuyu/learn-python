lower_bound = 1
upper_bound = 100

def isPrimeNumber(n):
	#documentation
	"""
	判读实数是否是素数	
	"""
	if n <= 1:
		return False
	for x in range(2,n-1):
		if n%x == 0:
			return False
	return True

def listPrimeNmbers(b, e):
	for x in range(b, e):
		if isPrimeNumber(x):
			print(x, end=' ', flush=True)
	print('')


#变长参数
def foo(*args):
	print(type(args))
	if len(args):
		for arg in args:
			print(arg, end=' ', flush=True)
	else:
		print('no argments')


def goo(**kwargs):
	print(type(kwargs))
	if len(kwargs) > 0:
		for k in kwargs:
			print(f'k:{k} v:{kwargs[k]}')
	else:
		print('no argments')




def main():
	#listPrimeNmbers(lower_bound, upper_bound)
		
	foo()
	foo('hello world', 3.14159, 99, True, None)
	print()
	args = ('hello world', 3.14159, 99, True, True)
	foo(*args)
	print()

	goo()
	goo(uk='United Kingdom', cn='China', pi=3.14159)
	kwargs = {'uk':'United Kingdom', 'cn':'China', 'pi':3.14159}
	goo(**kwargs)

if __name__ == '__main__':
	main()