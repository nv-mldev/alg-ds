def square_root(x):
    '''
    Function to calculate the square root of a number using Newton's method
    '''
    guess = x / 2
    while abs(guess**2 - x) > 0.0001:
        guess = (guess + (x / guess)) / 2
    return guess