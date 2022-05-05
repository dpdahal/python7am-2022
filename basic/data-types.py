# number
# string
# boolean
# list
# set
# tuple
# dis
# None

# number: integer, float, complex

# x = 10
# print(type(x))
# print(dir(x))

# y = 30.5
# print(dir(y))
# print(type(y))

#
# a = 20j
#
# print(type(a))

# x = input("Enter number: ")
# print(x)

# name
# address
# phone

#
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))

# x = int(x)
# y = int(y)
# print(x + y)
# print(type(x))

# x = '10'
# y = 20
# print(int(x) + y)


# name = input("Enter name: ")
# age = int(input("Enter age: "))
# # print("My name is:  {} age: {} ".format(name, age))
# print(f"My name is: {name} age: {age}")
# print("My name is " + name + "age " ,age)


# x = 10
# y = 20
# z = x
#
#
# print(y)
# print(z)
# print(x)

# name = "Sophia"
# print(name[90])
# print(name.upper())
# print(dir(name))
# print(type(name))

# print(100 > 20)

# x = None
# print(x)

# x, y = 10, 30

# name, age = input("Enter data name,age: ").split()
# print(name)
# print(age)

# data = [1, 3, 45, 'ram', 'sita']
# print(data[4])
#
# data[2] = "Hari"
# print(data)

# data = [1, 2, 3, 4]
# data.append(23)
# print(data)
# print(type(data))
# data[2] = 50
# print(data)
# print(dir(data))
# print(data[5])

# data = []  # Empty list
# data.append(20)
# print(data)
# data[0] = 30
# print(data)

# data = [1, 2, 3, 4, 5]
# print(data)
# data.clear()
# print(data)

# data = [1, 2, 3, 4, 5]
# d1 = [56, 67, 87]
# data.append(d1)
# print(data)
# print(data.pop())

# print(dir([]))

# data = ["anil", "ram", 10, 2, 3, 4]
# print(len(data))

# print(dir(data))
# print(data[:1])
# data.remove()
# data.remove('ram')
# print(data)
# d1 = [12, 34]
# data.extend(d1)
# print(data)
# data.insert(1, ['hari'])
# print(data)
# data[1]='sita'
# print(data)

# a = data.copy()
# print(a)
# print(len(data))
# data.sort(reverse=True)
# print(data)
# print(data.count(1))


# data = [
#     [1, 2, 3, 4],
#     [2, 3, 56, 78],
#     [23, 45, [67, [67, [900]]]]
# ]

# print(data[2][2][1][1][0])
# print(data[1][3])


# data = [1, 2, 3]

# data = (1, 2, 3)
# print(dir(data))
# data[0]=20

# data = {1, 2, 3, 1}
# print(data)

# data = {
#     "name": "ram",
#     "age": 20
# }
#
# print(data['name'])
# print(type(data))


users = {
    "name": 'Sophia',
    "address": {
        "location": "kathmandu"
    }
}
print(users['address']['location'])
