# Write a deterministic program, deterministicNumber, that returns an even number between 9 and 21.

# def deterministicNumber():
#     '''
#     Deterministically generates and returns an even number between 9 and 21
#     '''
#     # Your code here

import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    # Your code here
    return random.randrange(10, 21, 2)