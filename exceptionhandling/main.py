# print(10 / 0)


# try:
#     print(10 / 20)
# except Exception as e:
#     print('Exception:', e)
#
# finally:
#     print('finally')

# ZeroDivisionError
# ValueError
# IndexError


def add(x, y):
    if y == 0:
        raise Exception('y cannot be zero')
    return x + y


try:
    print(add(10, 0))
except Exception as e:
    print('Exception:', e)
