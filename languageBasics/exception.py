

def main():
	try:
		#x = 5/0
		#i = int('sfsf')
		#y = "hello" + 5
		print('hello world')
	except ZeroDivisionError:
		print("get a divide by zero error.")

	except ValueError as e:
		print(f"invalid arg: {e}")

	except Exception as e:
		print(f"got a error: {e}")
	
	else:
		print('no exception')

	finally:
		print('allways run')


if __name__ == '__main__':
	main()




