from curses import wrapper
from functools import wraps
#Review function and object in python
#returning functions from within functions
def bark(sound='hooooo'):
    def dog_bark():
        return "dog is barking"
    def wolf_bark():
        return "wolf is barking"
    if sound=='hooooo':
        return wolf_bark
    else:
        return dog_bark

#call bark function, bark() will only outut the function current address
whom_bark=bark()

#whom_bark will point to the address of wolf_bark function
#output the address, if change sound to other, would point to 
#dog_bark function
print(whom_bark)

#print out wolf is barking
print(whom_bark())
#or bark()(), add one more parenthesis
print(bark()())

#function as an argument
def no_sound():
    print('the animal is quiet')
def give_shot(func):
    print("vet is here")
    print(func())

give_shot(no_sound)
give_shot(bark())


def f1(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper
@f1
def f():
    print("Hello")
#if above function without @f1 docstring notation, then do
''' 
f1(f)()
#or
print()
x=f1(f)#function aliasing
x()
'''
#with @f1
f()

#to pass argument
def f1(func):
    def wrapper(*args,**kwargs):
        print("Start")
        value=func(*args,**kwargs)
        print("End")
        return value
    return wrapper

@f1
def f(a,b=8):
    print(a,b)
@f1
def add(x,y):
    return x+y
print(add(9,5))

#practice
#1 
'''
    Write a Python program to make a chain of 
function decorators (bold, italic, underline etc.).
'''
def bold(fn):
    def wrapper():
        return "<b>" + fn() + "</b>"
    return wrapper

def italic(fn):
    def wrapper():
        return "<i>" + fn() + "</i>"
    return wrapper

def underline(fn):
    def wrapper():
        return "<u>" + fn() + "</u>"
    return wrapper
@make_bold
@make_italic
@make_underline
def hello():
    return "hello world"
print(hello())

#2
'''
    Make a decorator factory which returns a decorator that decorates functions with one argument. T
he factory should take one argument, a type, and then returns a decorator that makes function should 
check if the input is the correct type. If it is wrong, it should print("Bad Type") 
(In reality, it should raise an error, but error raising isn't in this tutorial). 
Look at the tutorial code and expected output to see what it is if you are confused (I know I would be.) 
Using isinstance(object, type_of_object) or type(object) might help.
'''
def type_check(correct_type):
    #put code here
    def check(function):
        def function_modified(*arg):
            if(isinstance(*arg,correct_type)): return function(*arg)
            else: print("Bad Type")
        return function_modified
    return check
            
@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])
