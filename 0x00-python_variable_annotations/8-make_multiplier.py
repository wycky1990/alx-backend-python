#!/usr/bin/env python3
'''Contains a function that multiplies a float by multiplier
'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Multiplies a float by multiplier Args:multiplier (float)

    '''

    def multiplier_func(number: float) -> float:
    '''Multiplies a float by multiplier
    '''    
        return multiplier * number

    return multiplier_func
