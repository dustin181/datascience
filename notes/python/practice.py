#Reverse a list
a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
b = a[::-1]
print(a)
print(b)

#reverse a dict
chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}
print(rank_dict)
print(chile_len_set)

#flatten a list of lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)

#list comprehension with multiple loops
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x for x in a if x > 4 if x % 2 == 0]
c = [x for x in a if x > 4 and x % 2 == 0]

#give an index to a list
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for i, flavor in enumerate(flavor_list):
    print('%d: %s' % (i + 1, flavor))

#shorter version of the above
for i, flavor in enumerate(flavor_list, 1):
    print('%d: %s' % (i, flavor))

#zip up two lists
names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]
for name, count in zip(names, letters):
    print(name, count)

#generator example
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

address = 'Four score and seven years ago...'
result = list(index_words_iter(address))
print(result)

#positional arguments
def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))

log('My numbers are', 1, 2)
log('Hi there')



