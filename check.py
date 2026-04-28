# products = {
#     'Laptop': 990,
#     'Smartphone': 600,
#     'Tablet': 250,
#     'Headphones': 70,
# }

# for product in products.items():
#     print(product)


# class Dog:  
#     def __init__(self, name):  
#         self.name = name

#     def bark(self):  
#         print(f"{self.name} says Woof!")  

# my_dog = Dog("Rex")
# print(my_dog.name)


# def create_spend_chart(categories):
#     title = 'Percentage spent by category'
#     lines = []
#     for l in range(10,1):
#         for c in categories:
#             withdrawsAmount = sum(l['amount'] for l in c.ledger if l['amount'] < 0 )
#             withDrawPercent = round((withdrawsAmount * 100) / c.get_balance())
#         lines.append(l,  )



