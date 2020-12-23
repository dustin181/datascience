# def recursion():
#     print("Hello World")
#     recursion()


def recursion(count):

    if count == 10:
        return 0
    else:
        print("Hello World")
        recursion(count + 1)

def rundescending(n):
    if(n == 0):
        return

    print(n)
    rundescending(n - 1)

def runascending(n):
    if(n == 0):
        return

    runascending(n - 1)
    print(n)

count = 0
recursion(count)

n = 3
rundescending(n)
print("Completed")

n = 3
runascending(n)
print("Completed")
