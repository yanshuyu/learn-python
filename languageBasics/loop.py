
citys = ['newyork', 'maiami', 'beijing', 'shanghai']
idx = 0

while idx < 4:
	print(citys[idx])
	idx += 1

print('\n')

for city in citys:
	print(city)

#loop control - continue, break, else



def Login(psw):
	pw = ''
	cnt = 0
	maxCnt = 5
	hasPermission = False
	
	while pw != psw:
		if cnt >= maxCnt:
			break
		pw = input(f'try to input correct password.({ maxCnt-cnt } times remainder)')
		cnt += 1
	else: #exit the loop normally
		hasPermission = True
	return hasPermission	


def main():
	dic = {'cn':'China', 'us':'America', 'uk':'English', 'jp':'Japan'}
	
	#for loop
	for k,v in dic.items():
		print('key={}, value={}'.format(k,v))

	for num in range(1,10,2):
		print(num)
	print(type(range(10)))

	#while else
	x=0
	while x < 10:
		print('x: {}'.format(x))
		x += 1
	else:
		print('exit with x: {}'.format(x))
	
	#while break else
	x=0
	while x < 10:
		print('x: {}'.format(x))
		x += 1
		if x > 5:
			break
	else:
		print("exit with x: {}".format(x))

	#while pass else
	x=0
	while x < 10:
		print('x: ', x)
		if x == 3:
			x += 2
			pass
		x += 1
	else:
		print('exit with x: ', x)


	#while continue else
	x=0
	while x < 10:
		print('x: ', x)
		if x == 3:
			x += 2
			continue
		x += 1
	else:
		print('exit with x: ', x)




	# passWord = 'yan717171'
	# while Login(passWord) != True:
	# 	print('Login failed!')
	# 	opt = input('try agagin? (y/n)')
	# 	if opt == 'n':
	# 		break;
	# else:
	# 	print('Login success.')



if __name__ == '__main__':
	main()