# types of function
# 1. Inbuilt function
# 2. User defined function

# Inbuilt function example:
# 1. abs()
# 2. pow()
# 3. max()
# 4. min()
# 5. round()
# print(dir(__builtins__))

# User defined function example:

# define function
# def my_function():
#     # function body
#     print("Hello World")
#
#
# # call function
# my_function()

# parameters example:

# def users(name, age, address):
#     print("Hello", name)
#     print("You are", age, "years old")
#     print("You live in", address)
#
#
# users("John", 30, "New York")

# def add(x, y):
#     print(x + y)
#
#
# add(40, 50)
# add(70, 80)

# optional parameters example:

# def add(x, y=0):
#     print(x + y)
#
#
# add(40)

# *args example:
# **kwargs example:

# def users(*names, **data):
#     print(names)
#     print(data)
#
#
# users("John", "Mary", "Peter", name="John", age=30, address="New York")

# def test():
#     print("Hello World")
#
#
# def get():
#     test()
#
#
# get()


# return types function

# def add(x, y):
#     return x + y
#
#
# print(add(40, 50))

# def users():
#     pass
#
#
# print(users())
#
# def add_sub(x, y):
#     tot = x + y
#     sub = x - y
#     return [tot, sub]
#
#
# print(add_sub(40, 50))

# x = 10
#
#
# def test():
#     global x
#     x = x + 30
#     print(x)
#
# test()
#
# print(x)

# inline function example:

# a = lambda x, y: x + y
# print(a(20, 30))
#
#
# def a(x, y):
#     return x + y
# a(20, 30)


# def fac(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fac(n - 1)
#
#
# print(fac(5))
# 5-1:4 =20
# 4-1:3 =60
# 3-1:2 =120

# nested function

#
# def users():
#     def name(new_name):
#         return f"I am {new_name}"
#
#     return name
#
#
# print(users()("ram"))
# a = users()
# print(a())
# print(type(a))


# def users():
#     yield 'ram'
#     yield 'shyam'
#     yield 'hari'
#
#
# a = users()
# print(a.__next__())
# print(a.__next__())
# for i in a:
#     print(i)

#
# def connection():
#     """
#     This is a connection function used to connect to the database
#     """
#     return True
#
#
# print(connection.__doc__)


def take_value():
    pass


def calculate():
    pass


def display():
    pass
