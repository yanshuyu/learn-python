x=1
y=1

#比较运算
if x > y:
	print('x > y, x is {} y is {}'.format(x, y))
elif x == y:
	print('x == y')
else:
	print('x < y, x is {} y is {}'.format(x, y))
print()


#逻辑运算 and or not
if x and y:
	print('both x and y evaluated True')
else:
	print('x and y are not both evaluated True')
print()

#is
print('object	id')
print(f'x	{id(x)}')
print(f'y 	{id(y)}')
if x is y:
	print('x and y is the same object')
else:
	print('x and y is not the same object')
print()

y='hello world'
print('object	id')
print(f'x	{id(x)}')
print(f'y 	{id(y)}')
if x is y:
	print('x and y is the same object')
else:
	print('x and y is not the same object')
print()