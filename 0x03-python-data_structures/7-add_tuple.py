#!/usr/bin/python3.8
def add_tuple(tuple_a=(), tuple_b=()):
    a_first = tuple_a[0] if len(tuple_a) > 0 else 0
    a_second = tuple_a[1] if len(tuple_a) > 1 else 0
    b_first = tuple_b[0] if len(tuple_b) > 0 else 0
    b_second = tuple_b[1] if len(tuple_b) > 1 else 0

    # Calculate the sum of each corresponding element
    result_first = a_first + b_first
    result_second = a_second + b_second

    # Return the result as a tuple
    return (result_first, result_second)
