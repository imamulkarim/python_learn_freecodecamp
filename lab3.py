full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return 'The character name should be a string'
    if name == '':
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if name.find(' ') >0:
        return 'The character name should not contain spaces'

    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'All stats should be integers'
    if strength <1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    if strength >4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    if (strength + intelligence + charisma) != 7:
        return 'The character should start with 7 points'

    def full_dot_expand(full_dot, number):
        return full_dot.ljust(number, full_dot);
    character_detail = f'''{name}
    STR {full_dot_expand(full_dot, strength).ljust(10,empty_dot)}
    INT {full_dot_expand(full_dot, intelligence).ljust(10,empty_dot)}
    CHA {full_dot_expand(full_dot, charisma).ljust(10,empty_dot)}
    '''
    return character_detail

print(create_character('ren', 4, 2, 1))


 #character_detail = f'{name}\nSTR {full_dot_expand(full_dot, strength).ljust(10,empty_dot)}\nINT {full_dot_expand(full_dot, intelligence).ljust(10,empty_dot)}\nCHA {full_dot_expand(full_dot, charisma).ljust(10,empty_dot)}'


def greet():
    pass
    
print(greet())

message = 'Python is fun!'

print(message[0:6]) 

example_list = ['example', 'dashed', 'name']

joined_str = ' '.join(example_list)
print(joined_str)  # ?

int_1 = 4
int_2 = 2

print(int_1 ** int_2) # ?

developer = 'Jessica'

print(list(developer))

numbers = [1, 2, 3, 4, 5, 5, 5]
numbers.remove(5)

print(numbers)

