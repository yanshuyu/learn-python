


def pow2(x):
    return x**2

def add(x,y):
    return x+y

if __name__ == "__main__":
    numbers = [1, 2.2, 5, 7, 9]
    mapnumbers = map(pow2, numbers)
    print('numbers before map: ', numbers)
    print('map numbers: ', mapnumbers, [e for e in mapnumbers])
    print('numbers after map: ', numbers)

    arr1 = [1,2,3]
    arr2 = [4,5,6]
    print('arr1 + arr2: ', [e for e in map(add, arr1, arr2)])
