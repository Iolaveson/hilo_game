import random

class Draw:
    ''''''
    def drawn_card():
        '''picks a number at random'''
        number = random.randint(1,13)
        return number

    def new_card():
        '''picks a different number at random'''
        n_number = random.randint(1,13)
        return n_number