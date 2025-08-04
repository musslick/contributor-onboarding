from typing import Optional
import numpy as np

# TODO: make all functions work with strings as well
# TODO: add a new cool calculator function

def sum(a: int, b: int) -> int:
    '''
    This function returns the sum of two numbers

    Args:
    a: float the first number
    b: float the second number

    Returns:
    float the sum of a and b
    '''
    return a + b

def multiply(a, b) -> float:
    '''
    This function returns the product of two numbers

    Args:
    a: float the first number
    b: float the second number

    Returns:
    float
    '''
    return a * b

def divide(a: float, b: float) -> float:
    '''
    ...

    Args:
    a: float the number to be divided
    b: float the divisor

    Returns:
    float
    '''
    return a / b

def modulo(a: int, b: int):
    '''
    ...

    Args:
    a: int the number to be divided
    b: int the divisor

    Returns:
    float
    '''

    # I think this could be made more efficient?
    result = a - (np.floor(a / b) * b)

    return result

def element_wise_multiply(a: np.array, b: np.array) -> np.array:
    '''
    ...

    Args:
    a: np.array
    b: np.array

    Returns:
    np.array
    '''

    # let's hope that both vectors have the same shape

    return np.multiply(a, b)

def return_hexadecimal(a: int) -> float:
    '''
    ...

    Args:
    a: float
    b: float

    Returns:
    float
    '''

    return hex(a)


def return_random_number(a: int, b:int) -> int:
    '''
    ...

    Args:
    a: float
    b: float

    Returns:
    float
    '''

    return np.random.randint(a, b)