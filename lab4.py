def number_pattern(n):
    if(not isinstance(n, int)):
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    n_loop = ''
    for number in range(n):
        n_loop += f'{str(number+1)} '

    return n_loop.rstrip()



print(number_pattern(4))