my_str1 = 'hello world'
my_str2 = "hello python"
print(my_str1, my_str2)

#indexing
print(my_str1[1])
print(my_str2[-1])

#slicing
print(my_str1[1:])
print(my_str1[:-1])
print(my_str1[:])
print(my_str1[::2])
print(my_str1[::-1])

#immutable
#my_str1[0]='H'


#object method
print(my_str1.upper())
print(my_str1)

print(my_str1.lower())
print(my_str1)

print(my_str2.split())