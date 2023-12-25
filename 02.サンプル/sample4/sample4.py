import doctest

def div2(a, b):
    '''
    2.0になるように割る
    >>> div2(1.2, 0.6)
    2.0

    0で割る
    >>> div2(1.2, 0.0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: float division by zero
    '''

    return a / b


if __name__ == '__main__':
    doctest.testmod()
