


if __name__ == '__main__':
    numbers = [2,13,55,46,32,88,49]
    print('filter numbers with even: ', [ e for e in filter(lambda x: True if x%2==0 else False, numbers)])