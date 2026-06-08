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



# my_set_var = {7, 5, 8, 5}
# print(my_set_var)  # Output: {8, 5, 7} (order may vary)

# my_dictionary_var = {"name": "Alice", "age": 25, "name": "Bob"}
# print('Dictionary:', my_dictionary_var) # Dictionary: {'name': 'Alice', 'age': 25}

# my_tuple_var = (7, 5, 8,5)
# print('Tuple:', my_tuple_var) # Tuple: (7, 5, 8)

# message = 'Python is fun!'

# print(message[0:6])  # Python
# print(message[7:])  # is fun!
# print(message[::-1])  # !nuf si nohtyP

# cities = ['Los Angeles', 'London', 'Tokyo']
# print(cities[0]) # Los Angeles

# developer = ['Alice', 34, 'Rust Developer']
# name, *rest = developer
# print(rest) # 

# numbers = [1, 2, 3, 4, 5, 6]
# print(numbers[1::2]) # [2, 4, 6]

# numbers = [1, 2, 3, 4, 5]
# numbers.pop() # The number 5 is returned
# print(numbers) # [1, 2, 3, 4]

# numbers = [1, 2, 3, 4, 5]
# print(numbers.find(3)) # [2, 3, 4]

# complex = 1 + 2j # todo
# print(complex.real)  # Output: 1.0
# print(complex.imag)  # Output: 2.0
# python numeric data types: int, float, complex
# python immutable data types: int, float, complex, str, tuple, frozenset
# python mutable data types: list, dict, set

# What is the result of evaluting set("lane") == set("anneal")?
# my_set_var = set("lane") 
# my_set_var2 = set("anneal")
# print (len(my_set_var)) # 1
# print (my_set_var) # {'l', 'a', 'n', 'e'}
# print (my_set_var2) # {'l', 'a', 'n', 'e'}
# print(my_set_var == my_set_var2)  # Output: True (both sets contain the same unique characters)


# dd = 2/2
# print(dd) # 1.0



# if not "yay" or "yass":
#     print("yay") # yay

# vvde = 3/True
# print(vvde) # 3.0

#Sets: Unordered collections of unique elements. No duplicates allowed, no specific order maintained.
# my_set_var = {"lane", "lane"}
# print(my_set_var)  # Output: {'lane'} (duplicates are removed) 


# TypeError: Can't instantiate abstract class ConcreteClassOne without an implementation for abstract method 'abstract_method'
#from abc import ABC, abstractmethod
# import abc

# # Define an abstract base class
# class AbstractClass(abc.ABC):
#     @abc.abstractmethod
#     def abstract_method(self):
#         print('Implementation in abstractClassOne')

# # Concrete subclass that implements the abstract method
# class ConcreteClassOne(AbstractClass):
#     # def abstract_method(self):
#     #     print('Implementation in ConcreteClassOne')

#     def another_method(self):
#         print('Another method in ConcreteClassOne')

# cco = ConcreteClassOne()
# cco.abstract_method()  # Output: Implementation in ConcreteClassOne


#* It's also efficient for finding all neighbor nodes, since this operation only requires accessing the list associated to the node.
#* - Adjacency lists are less efficient than adjacency matrices for determining if there is an edge between two nodes.

# Which error occurs when you use a variable that has not been defined?
# A) NameError (Answer: A)
# B) TypeError
# C) ValueError
# D) KeyError


# for i in {'a':1, 'b':2, 'c':3}:
#     print(i) # a b c # Again i select the wrong answer


# fruits = ['apple', 'pear', 'banana', 'orange']
# fruits.insert(2, 'plum')
# fruits.pop()
# fruits.append('kiwi')

# print(fruits) # ['apple', 'pear', 'plum', 'banana', 'kiwi']


# Which of the following Big O notations represents the fastest growing function?
# todo:
# A) O(2n)
# B) O(n log n)   
# C) O(1)
# D) O(n2) 

# what is the output of the following code snippet?
# my_list = [3.99, '42', True]
# my_new_list = [int(i) for i in my_list]
# print(my_new_list) # [3, 42, 1]


# What is the output of the following code snippet? print('2025/07/' + 25)
# A) 2025/07/25
# B) TypeError: can only concatenate str (not "int") to str (Answer: B)
# C) ConcatenationError
# D) 20250725