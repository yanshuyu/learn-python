def sum(x,y):
    return x+y


if __name__ == '__main__':
    scores = [1,2,3,4,5,6,7,8,9]
    print('sum of {} is {}'.format(scores, reduce(sum, scores)))