
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


def x_fizz_buzz__mutmut_orig(n):
    if n % 15 == 0:
        return 'fizz buzz'

    if n % 3 == 0:
        return 'fizz'

    if n % 5 == 0:
        return 'buzz'
def x_fizz_buzz__mutmut_1(n):
    if n / 15 == 0:
        return 'fizz buzz'

    if n % 3 == 0:
        return 'fizz'

    if n % 5 == 0:
        return 'buzz'
def x_fizz_buzz__mutmut_2(n):
    if n % 16 == 0:
        return 'fizz buzz'

    if n % 3 == 0:
        return 'fizz'

    if n % 5 == 0:
        return 'buzz'
def x_fizz_buzz__mutmut_3(n):
    if n % 15 != 0:
        return 'fizz buzz'

    if n % 3 == 0:
        return 'fizz'

    if n % 5 == 0:
        return 'buzz'
def x_fizz_buzz__mutmut_4(n):
    if n % 15 == 1:
        return 'fizz buzz'

    if n % 3 == 0:
        return 'fizz'

    if n % 5 == 0:
        return 'buzz'
def x_fizz_buzz__mutmut_5(n):
    if n % 15 == 0:
        return 'XXfizz buzzXX'

    if n % 3 == 0:
        return 'fizz'

    if n % 5 == 0:
        return 'buzz'
def x_fizz_buzz__mutmut_6(n):
    if n % 15 == 0:
        return 'fizz buzz'

    if n / 3 == 0:
        return 'fizz'

    if n % 5 == 0:
        return 'buzz'
def x_fizz_buzz__mutmut_7(n):
    if n % 15 == 0:
        return 'fizz buzz'

    if n % 4 == 0:
        return 'fizz'

    if n % 5 == 0:
        return 'buzz'
def x_fizz_buzz__mutmut_8(n):
    if n % 15 == 0:
        return 'fizz buzz'

    if n % 3 != 0:
        return 'fizz'

    if n % 5 == 0:
        return 'buzz'
def x_fizz_buzz__mutmut_9(n):
    if n % 15 == 0:
        return 'fizz buzz'

    if n % 3 == 1:
        return 'fizz'

    if n % 5 == 0:
        return 'buzz'
def x_fizz_buzz__mutmut_10(n):
    if n % 15 == 0:
        return 'fizz buzz'

    if n % 3 == 0:
        return 'XXfizzXX'

    if n % 5 == 0:
        return 'buzz'
def x_fizz_buzz__mutmut_11(n):
    if n % 15 == 0:
        return 'fizz buzz'

    if n % 3 == 0:
        return 'fizz'

    if n / 5 == 0:
        return 'buzz'
def x_fizz_buzz__mutmut_12(n):
    if n % 15 == 0:
        return 'fizz buzz'

    if n % 3 == 0:
        return 'fizz'

    if n % 6 == 0:
        return 'buzz'
def x_fizz_buzz__mutmut_13(n):
    if n % 15 == 0:
        return 'fizz buzz'

    if n % 3 == 0:
        return 'fizz'

    if n % 5 != 0:
        return 'buzz'
def x_fizz_buzz__mutmut_14(n):
    if n % 15 == 0:
        return 'fizz buzz'

    if n % 3 == 0:
        return 'fizz'

    if n % 5 == 1:
        return 'buzz'
def x_fizz_buzz__mutmut_15(n):
    if n % 15 == 0:
        return 'fizz buzz'

    if n % 3 == 0:
        return 'fizz'

    if n % 5 == 0:
        return 'XXbuzzXX'

x_fizz_buzz__mutmut_mutants = {
'x_fizz_buzz__mutmut_1': x_fizz_buzz__mutmut_1, 
    'x_fizz_buzz__mutmut_2': x_fizz_buzz__mutmut_2, 
    'x_fizz_buzz__mutmut_3': x_fizz_buzz__mutmut_3, 
    'x_fizz_buzz__mutmut_4': x_fizz_buzz__mutmut_4, 
    'x_fizz_buzz__mutmut_5': x_fizz_buzz__mutmut_5, 
    'x_fizz_buzz__mutmut_6': x_fizz_buzz__mutmut_6, 
    'x_fizz_buzz__mutmut_7': x_fizz_buzz__mutmut_7, 
    'x_fizz_buzz__mutmut_8': x_fizz_buzz__mutmut_8, 
    'x_fizz_buzz__mutmut_9': x_fizz_buzz__mutmut_9, 
    'x_fizz_buzz__mutmut_10': x_fizz_buzz__mutmut_10, 
    'x_fizz_buzz__mutmut_11': x_fizz_buzz__mutmut_11, 
    'x_fizz_buzz__mutmut_12': x_fizz_buzz__mutmut_12, 
    'x_fizz_buzz__mutmut_13': x_fizz_buzz__mutmut_13, 
    'x_fizz_buzz__mutmut_14': x_fizz_buzz__mutmut_14, 
    'x_fizz_buzz__mutmut_15': x_fizz_buzz__mutmut_15
}

def fizz_buzz(*args, **kwargs):
    result = _mutmut_trampoline(x_fizz_buzz__mutmut_orig, x_fizz_buzz__mutmut_mutants, *args, **kwargs)
    return result 

fizz_buzz.__signature__ = _mutmut_signature(x_fizz_buzz__mutmut_orig)
x_fizz_buzz__mutmut_orig.__name__ = 'x_fizz_buzz'


