import random


def generate_matrix(rows, cols, num_range=(-10, 10)):
    return [[random.randint(*num_range) for x in range(0, cols)] for row in range(0, rows)]
