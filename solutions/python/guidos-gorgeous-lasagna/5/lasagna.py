"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40

def bake_time_remaining(cooking=0):
    
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - cooking


def preparation_time_in_minutes(number_of_layers=0):
    """Calculate the preparation time needed according to the number of lasagne layers

    :param number_of_layers: int - number of layers.
    :return: int - preparation time (in minutes) derived from 'number_of_layers'.

    Function that takes the number of lasagna layers as an argument and return the preparation time needed.
    """
    return number_of_layers * 2



def elapsed_time_in_minutes(number_of_layers=0, elapsed_bake_time=0):
    """Calculate the elapsed time according to the number of lasagne layers and the already elapsed baking time

    :param number_of_layers: int - number of layers.
    :param elapsed_bake_time: int - elapsed baking time.
    :return: int - elapsed baking time (in minutes) derived from 'number_of_layers and elapsed_bake_time'.

    Function that takes the number of lasagna layers and elapsed time as arguments and return the elapsed time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time