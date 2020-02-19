#!/usr/bin/env python

def get_message():
    return "Hello, BNP world"


x = get_message()
print(x)

def spam():
    name = "Bob"

s = spam()
print(s)


# m = get_message

def hello():
    print("HELLO EVERYBODY!")


hello()

def greet():
    message = get_message()
    print(message)

greet()

def add(x:int=50, y:int=100):  # parameters (or params)
    return x + y

print(add(5, 10))  # args
print(add('a', 'b'))  # args

result = add(25.4, 16.6)
print(result)

result = add(5)
print(result)

result = add()
print(result)

def poly(weasel, *args):
    print(args)

poly(1)
poly(1, 2, 3)
poly('fish', 'bear', 'moose', 'monkey')
# poly()






x = 100


def spam():
    y = 42

spam()

print("x =", x)
# print("y =", y)






