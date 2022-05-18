# .txt
# .bin
# .csv
# .json
# .xml
# .yaml

# file mode
# r - read
# w - write
# a - append
# r+ - read and write
# w+ - write and read
# a+ - append and read


# open('student.txt', 'w').close()

# handle = open('student.txt', 'a')
# handle.write("test was successful\n")
# handle.close()

# obj = open('student.txt', 'r')
# print(obj.readlines())
# obj.close()
# print(obj.readline())
# print(obj.read())

#
# with open('student.txt', 'r') as obj:
#     print(obj.readlines())

# obj = open('student.txt', 'w+')
# obj.write('test')
# print(obj.readlines())

# a = int(input('Enter a number: '))
# b = int(input('Enter a number: '))
# sum = a + b
#
# with open('student.txt', 'a') as obj:
#     obj.write(f'sum: {sum}\n')
