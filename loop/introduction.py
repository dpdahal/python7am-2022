"""
Repetitive execution of the same block of code over and over is referred to as iteration.
There are two types of iteration:
Definite iteration, in which the number of repetitions is specified explicitly in advance
Indefinite iteration, in which the code block executes until some condition is met
In Python, indefinite iteration is performed with a while loop.

Iterables
In Python, iterable means an object can be used in iteration. The term is used as:

An adjective: An object may be described as iterable.
A noun: An object may be characterized as an iterable.
"""
# while loop: indefinite iteration
# Example:

# x = 1
# while x < 10:
#     print(x)
#     x += 1

# num = int(input("Enter number: "))
# increment = 1
#
# while increment <= num:
#     print(f"{increment}: Sophia")
#     increment += 1

# WAP to enter number of time and print total even and odd sum

# total_even = 0
# total_odd = 0
# increment = 1
# num = int(input("Enter number: "))
#
# while increment <= num:
#     if increment % 2 == 0:
#         total_even += increment
#     else:
#         total_odd += increment
#
#     increment += 1
#
# print(f"Total even: {total_even}")
# print(f"Total odd: {total_odd}")


# data = ['ram', 'sita', 'gita', 'hari', 'laxmi', 'sophia']


# x = 0
# while x < len(data):
#     print(data[x])
#     x += 1

# ram

# print('a' in x)
#
# data = ['ram', 'sita', 'gita', 'hari', 'laxmi', 'sophia']
# for name in data:
#     print(name)
# a = iter(data)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(dir(data))

# for loop: definite iteration
# Example:
# for name in data:
#     print(name)


# data = [
#     ['ram', 'sita', 'gita', 'hari'],
#     ['laxmi', 'sophia', 'gopal', 'madan'],
#     ['krishna', 'kiran', 'krishna', 'kiran'],
# ]
#
# for nams in data:
#     for name in nams:
#         print(name)


# c,jva,php
# for(int x=0;x<10;x++){
#     System.out.println(x);
# }

# print(range(10))
# for x in range(10):
#     print(x)


# WAP to enter number of students enter
# five subject marks and print total marks and average marks
# of each student division wise
