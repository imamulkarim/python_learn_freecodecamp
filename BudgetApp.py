class Category:
    
    def __init__(self,name ):
        self.ledger = []
        self.name = name

    def deposit(self, amount, description=''):
        self.ledger.append({
            'amount' : amount,
            'description': description
        })

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False

        self.ledger.append({
            'amount' : -amount,
            'description': description
        })
        return True

    def get_balance(self):
        total = sum(l['amount'] for l in self.ledger )
        return total

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False

        self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f'Transfer from {self.name}')
        return True

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        ledger_text = ''
        for l in self.ledger:
            ledger_text += '\n' + l['description'][:23].ljust(23, ' ') + str(format(l['amount'], '.2f').rjust(7))
        ledger_text += '\nTotal: ' + str(self.get_balance())
        return self.name.center(30, '*') + ledger_text

def create_spend_chart(categories):
    bar_chart_str = 'Percentage spent by category'
    categories_num = len(categories) # Total no. of categories
    col_length = 12
    total_spending = 0

    category_names = [] # list of category names
    for cat in categories:
        category_names.append(cat.name)
        for entry in cat.ledger:
            for value in entry.values():
                if isinstance(value, (int, float)) and value < 0:
                    total_spending -= value
    
    #calculate Total Spending
    length = 0
    for name in category_names: # figuring what should be the length of our columns
        if len(name) > length:
            length = len(name)
    col_length += length


    # Creates the scale column
    scale = []
    for i in range(100, -1, -10):
        scale.append(f"{i}|".rjust(4))
    scale.append('    ')
    for i in range(col_length):
        scale.append('    ')

    # Creates other columns
    columns = []
    for category in range(categories_num):
        temp = []
        association = {100: 0, 90: 1, 80: 2, 70: 3, 60: 4, 50: 5, 40: 6, 30: 7, 20: 8, 10: 9, 0: 10}

        category_spending = 0
        for entry in categories[category].ledger:
            for value in entry.values():
                if isinstance(value, (int, float)) and value < 0:
                    category_spending -= value

        category_percent = (category_spending/total_spending) * 100
        
        import math
        rounded_cat_percent = math.floor(category_percent/10) * 10

        for val in range(association[rounded_cat_percent]):
            if category == categories_num - 1:
                temp.append('    ')
            else:
                temp.append('   ')

        # it creates the list of graph dots.
        for val in range((11-len(temp))):
            if category == categories_num - 1: # Conditional to add two spaces after the last column
                temp.append(' o  ')
            else:
                temp.append(' o ')
        if category == categories_num - 1:
            temp.append('----')
        else:
            temp.append('---')


        # adds name of category to the columns list
        category_name = list(category_names[category])
        for ch in category_name:
            if category == categories_num - 1:
                temp.append(' ' + ch + '  ')
            else:
                temp.append(' ' + ch + ' ')

        # makes sure that all columns are of same length
        if len(temp) == col_length:
            columns.append(temp)
        else:
            for i in range((col_length - len(temp))):
                temp.append('   ')
            columns.append(temp)

    # Conatinates all columns to the final string
    for i, col in enumerate(zip(*columns)):
        bar_chart_str += f"\n{scale[i]}{''.join(col)}"
    
    return bar_chart_str


food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
# print(food.get_balance())
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)