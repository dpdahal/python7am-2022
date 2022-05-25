class Mobile:

    def __init__(self, company_name):
        print(company_name)

    def brand(self, brand):
        return f'Brand {brand}'

    def model(self, model):
        return f'Model {model}'

    def price(self, price):
        return f'Price {price}'


class Demo:
    def __init__(self, company_name, location):
        print("test")


class Mi(Demo,Mobile):
    def __init__(self, company_name, logo):
        # Mobile.__init__(self, company_name)
        # super().__init__(company_name)
        Demo.__init__(self, company_name, logo)
        Mobile.__init__(self, company_name)
        print(logo)

    def memory(self, memory):
        return f'Memory {memory}'


obj = Mi('Xiaomi', 'X')
# print(obj.brand('Xiaomi'))
