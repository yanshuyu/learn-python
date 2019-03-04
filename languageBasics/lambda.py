revertstr = lambda s : s[::-1]

iseven = lambda num : num % 2 == 0

firstChar = lambda strs : [s[0] for s in strs]

greater = lambda x,y : x > y


print(type(revertstr))

print(revertstr('hello world'))

print(firstChar(['hello', 'world']))

print(greater(5, 2))