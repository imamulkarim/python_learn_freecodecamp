# Build a User Configuration Manager


def add_setting(setting_dic, kv_tuple):
    if not isinstance(kv_tuple, tuple) and kv_tuple.count(0) != 1:
        return f'Incorrect parameter format kv_tuple: {kv_tuple}'
    key, value = kv_tuple
    key = key.lower();
    value = value.lower();

    if key in setting_dic:
        return f'Setting \'{key}\' already exists! Cannot add a new setting with this name.'

    setting_dic[key] = value
    return f'Setting \'{key}\' added with value \'{value}\' successfully!'


def update_setting(setting_dic, kv_tuple):
    if not isinstance(kv_tuple, tuple) and kv_tuple.count(0) != 1:
        return f'Incorrect parameter format kv_tuple: {kv_tuple}'
    key, value = kv_tuple
    key = key.lower();
    value = value.lower();

    if not key in setting_dic:
        return f'Setting \'{key}\' does not exist! Cannot update a non-existing setting.'

    setting_dic[key] = value
    return f'Setting \'{key}\' updated to \'{value}\' successfully!'


def delete_setting(setting_dic, key):
    
    key = key.lower()

    if not key in setting_dic:
        return f'Setting not found!'

    setting_dic.pop(key)
    return f'Setting \'{key}\' deleted successfully!'



def view_settings(setting_dic):
    if not isinstance(setting_dic, dict) or not setting_dic:
        return f'No settings available.'

    
    current_settings = ''
    for key,value in setting_dic.items():
        current_settings += key.capitalize() + ": " + value + "\n"

    current_settings = 'Current User Settings:\n' +  current_settings 

    return current_settings


test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}

#print(view_settings(test_settings))

print(add_setting(test_settings, ('language', 'english')))

print(update_setting(test_settings, ('theme', 'dark')))

print(delete_setting(test_settings, 'Language'))

print(view_settings(test_settings))