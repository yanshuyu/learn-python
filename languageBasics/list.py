myList = ['a','b','c','d','E','F','G']
print(myList)

#indexing
print(myList[0])

#slicing
print(myList[1:])
print(myList[:-1])
print(myList[::2])

#concatination
myList += ['1','2','3']
print(myList)

#len
print(len(myList))

#methods
myList.clear()
print(myList)

myList.append('append object')
print(myList)

myList += ['hello world', 'python', 'c++', 1, 3.14]
print(myList)

myList.reverse()
print(myList)

#myList.sort()
#print(myList)

myList.pop()
print(myList)

#comprehension
row1 = [1,0,0,0]
row2 = [0,1,0,0]
row3 = [0,0,1,0]
row4 = [0,0,0,1]
matrix = [row1, row2, row3, row4]
print(matrix)

colVector = [row[0] for row in matrix]
print(colVector)