# class College:
#     def __init__(self, name, location):
#         self._name = name
#         self.__location = location
#
#
# class Student(College):
#     def info(self):
#         print(self._name)
#         print(self.__location)
#     # public, private, protected: java,php,c#
#     # def __init__(self, myname, age):
#     #     self.__name = myname
#     #     self.age = age
#     #
#     # def __getName(self):
#     #     return self.__name
#
#
# obj = Student("ram", 20)
# obj.info()
# # print(obj.__getName())
#
# #  __int__()


# class College:
#     __name = 'hari'
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     # def __delete__(self):
#     #     del self.__name
#
#
# obj = College()
# obj.set_name('sophia')
# print(obj.get_name())

# del obj
# print(obj.get_name())

#
# class Employee:
#     def __new__(cls, *args, **kwargs):
#         print('I am Employee new method')
#         return object.__new__(cls)
#
#     def __init__(self):
#         print('I am Employee')
#
#     def __repr__(self):
#         pass
#
#     def __str__(self):
#         print('Employee')
#
#     def __call__(self, *args, **kwargs):
#         print('I am Employee call method')
#
#
# # def __init__(self):
# #     print("I am in init")
# #
# # def __del__(self):
# #     print("I am in del")
#
#
# obj = Employee()
# obj()
# print(obj)


# class Employee:
#     enm_name = ''
#
#     @property
#     def test(self):
#         return f"My name is {self.enm_name}"
#
#     @test.setter
#     def test(self, name):
#         self.enm_name = name
#
#     @test.deleter
#     def test(self):
#         del self.enm_name
#
#
# obj = Employee()
# obj.test = 'sophia'
# print(obj.test)
# del obj.test
# print(obj.test)

# class Employee:
#
#     @staticmethod
#     def emp_name():
#         return 'sophia'
#
#     @staticmethod
#     def add(x, y):
#         return x + y
#
#
# Employee.emp_name()
# print(Employee.add(20, 30))


# class Test:
#     a = 10

# @classmethod
# def get(cls):
#     cls.a

# def __repr__(self):
#     pass
#
# def __add__(self, other):
#     pass


# class User(object):
#     pass


# import datetime
#
# print(datetime.datetime.now())
