print("Welcome to my world")
print(2+3)
f="Pythonp"
print(f.index("P"))
print(f.replace("t","new"))
print(None==[])
a=5
assert a>4, "The value of a is too small"
print(a)
for i in range(1,5):
    if i==3:
        break
    print(i)


class Myclass:
    def ab(self):
        print("Hello")
ob = Myclass()
print(ob.ab)
ob.ab()

globvar = 10
def read1():
    print(globvar)
def write1():
    global globvar
    globvar=5
    print(globvar)
def write2():
    globvar = 15
    print(globvar)

read1()
write1()
read1()
write2()
read1()

f=5
print(f)
f="Check"

print(f)
print(f, type(f))
print(isinstance(f, str))

t=[1,2.2,'Mahesh']
print(t[0])
t[1]=3
print(t[1])

print(set(t))
print(tuple(t))
print(t)
print(dict([[1,2],[3,4]]))

num1 = 6564424525
num2 = 323252462

print(int(num1)+int(num2))



def is_leap(year):
    if year%4!=0:
        print(str(year)+" is not a multiple of 4 hence it's not a leap year.")
    if year%100!=0:
        print(str(year)+ " is not a multiple of 100 hence it's not a leap year.")
    if year%400!=0:
        print(str(year)+ " is not a multiple of 400 hence it's not a leap year.")
    else:
        print(str(year)+" ia s Leap Year")
 #print(leap)

is_leap(1900)


def is_leap(year):
    leap = False

    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        leap = True
    else:
        leap = False

    return leap


n=int(input("Range:"))
print("{}".format(pow(n, 2)))



n = int(input("Number:"))
print(*range(1, n+1), sep=' ')



password = 'India'
guess = ''
guess_count=0
limit=3

while password !=guess and guess_count<limit:
    guess = input("Enter password:")

    if password !=guess:
        print("Wrong Passowrd.Re-Type it ! ")
        guess_count += 1

if guess_count>=limit:
    print('Limit exceeded')
else:
    print("Loading!!!!")

numbers=[[1,2,3],[4,5,6],[0]]
print(numbers[2][1])













