# def decorator(fun):
#     def wrapper(*args,**kwargs):
#         print("Wrapping is done before")
#         fun(*args,**kwargs)
#         return fun
#     return wrapper
#
# @decorator
# def add(x,y):
#     a = print("The sum of {} and {} is : {}".format(x,y,x+y))
#     return a
#
# @decorator
# def sub(x,y):
#     a = print("The difference {} and {} is : {}".format(x,y,x - y))
#     return a
#
# class decorator_class(object):
#     def __init__(self,fun):
#         self.fun = fun
#     def __call__(self, *args, **kwargs):
#         return self.fun(*args,**kwargs)
#
# @decorator_class
# def Mul(x,y):
#     a = print("The product of {} and {} is : {}".format(x,y,x*y))
#     return a
#
# @decorator_class
# def div(x,y):
#     a = print("The diviion {} and {} is : {}".format(x,y,x//y))
#     return a
#
# class Coordinate(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         return "Coord: " + str(self.__dict__)
# def add(a, b):
#     return Coordinate(a.x + b.x, a.y + b.y)
# def sub(a, b):
#     return Coordinate(a.x - b.x, a.y - b.y)
# one = Coordinate(100, 200)
# two = Coordinate(300, 200)
#
# print(add(one, two))



def decorator(fun):
    def wrapper(*args,**kwargs):
        print('sorted mobiles are:')
        print(*sorted(fun(*args,**kwargs)), sep='\n')
    return wrapper


@decorator
def mobile_format(n):
    r=("+91 {} {}".format(i[-10:-5],i[-5:])for i in n)
    return r

# number=[input() for x in range(int(input("Enter Mobile Numbers:")))]
# mobile_format(number)

class decorator_class(object):
    def __init__(self,fun):
        self.fun=fun
    def __call__(self, *args, **kwargs):
        print("Sorted Mobiles Numbers:")
        print(*sorted(self.fun(*args,**kwargs)), sep='\n')



@decorator_class
def mobile_format(n):
    r=("+91 {} {}".format(i[-10:-5],i[-5:])for i in n)
    return r

# number=[input() for x in range(int(input("Enter Mobile Numbers:")))]
# mobile_format(number)

def wrapper(f):
    def fun(l):
        r=f("+91 {} {}".format(n[-10:-5],n[-5:])for n in l)
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input("Numbers:")))]
    sort_phone(l)


