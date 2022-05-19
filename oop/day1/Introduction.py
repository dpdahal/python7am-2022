# # declare a class
# class Introduction:
#     # body part of the class
#     x = 10
#
#     def test(self):
#         pass
#
# # declare an object: instance of the class
# obj = Introduction()
# # access the object
# print(obj.x)
# print(obj.test())
#
#


# class Students:
#     pass
#
#
# obj = Students()
# obj.name = 'John'
# obj.age = 20
#
# print(obj.name)
# print(obj.age)


# class Students:
#     def name(self, name):
#         print(f'Student name is {name}')
#
#     def age(self, age):
#         print(f'Student age is {age}')
#
# ojb = Students()
# ojb.name('John')
# ojb.age(20)
# ojb.name('sita')
# ojb.age(30)

# obj = Students()
# obj.name = 'John'
# obj.age = 20

# print(obj.name)
# print(obj.age)


# class User:
#     name = 'Sophia'
#
#     def get_name(self):
#        print(self.name)
#        print(self.age())
#
#     def age(self):
#         return 10
#
#
# obj = User()
# obj.get_name()


class Introduction:
    total = 0

    def __init__(self, name, age):
        print(name, age)
        Introduction.total += 1


obj = Introduction('John', 20)
obj1 = Introduction('sita', 20)
obj2 = Introduction('gita', 20)
obj3 = Introduction('hari', 20)

print(obj.total)
