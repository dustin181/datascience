def square(num):
    return num ** 2

def greater(num):
    return num > 39

sum = lambda x, y: x + y
print(sum(10,20))

lst = [5, 10, 20, 25, 50]
print(list(map(square, lst)))
print(list(map(lambda num: num ** 2, lst)))

lst = [37,38,42,40,39,45]
print(list(filter(greater, lst)))
print(list(filter(lambda num: num > 39, lst)))

lst = [5, 10, 15, 20, 25]

from functools import reduce
print(reduce(lambda x, y: x + y, lst))


