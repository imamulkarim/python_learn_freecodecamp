def fibonacci(n:int):
    if n < 0:
        raise ValueError('n must be a non-negative integer')

    if n == 0:
        return 0
    if n == 1:
        return 1
    sequence = [0, 1]

    for i in range(1 , n):
        sequence.append( sequence[-1]+ sequence[-2] )

    return sequence[-1]



print(fibonacci(15))

# 0 1 1