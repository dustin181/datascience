# def div(a, b):
#     return a/b
#
# def check(func):
#     def inner(a, b):
#        if b > a:
#            return b/a
#        func(a, b)
#     return inner
#
# print(div(2,10))

# div = check(div)
# print(div(2,10))
# # result = 5



def check(func):
    def inner(a, b):
        if b > a:
            return b/a
        return func(a, b)
    return inner

@check
def div(a, b):
    return a/b

print(div(10,2))