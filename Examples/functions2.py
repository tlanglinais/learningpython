# my solutions to the udemy functions exercises section
# <----1---->

def contains_purple(*args):
    if 'purple' in args:
        return True
    return False

# <----2---->

def combine_words(word, **kwargs):
    if 'prefix' in kwargs:
        word = kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        word = word + kwargs['suffix']
    return word


# <----3---->

# <----4---->

# <----5---->

# <----6---->

# <----7---->

# <----8---->
def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final