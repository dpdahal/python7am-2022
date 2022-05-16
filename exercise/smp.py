# def take_value():
#     p = int(input("Enter p : "))
#     t = int(input("Enter t : "))
#     r = int(input("Enter r : "))
#     return [p, t, r]
#
#
# def calculate():
#     # p, t, r = take_value()
#     # return p * t * r / 100
#     res = take_value()
#     p = res[0]
#     t = res[1]
#     r = res[2]
#     return p * t * r / 100
#
#
# def display():
#     print("The interest is : ", calculate())
#
#
# display()
#
# name = input("Enter name: ")
# time = int(input("Enter time: "))
#
#
# def my_repeat(data, n_times):
#     increment = 1
#     while increment <= n_times:
#         print(data)
#         increment += 1
#
#
# my_repeat(name, time)

# define function like: add_sub_multiply_divide(a, b)


# def add_sub_mul_div(x, y):
#     add = x + y
#     sub = x - y
#     mul = x * y
#     div = x / y
#     return [add, sub, mul, div]
#
#
# result = add_sub_mul_div(20, 30)
# print(f"total add: {result[0]}, total sub: {result[1]}, total mul: {result[2]}, total div: {result[3]}")

print(dir(__builtins__))