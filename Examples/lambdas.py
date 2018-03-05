# my solutions to the udemy functions exercises section
# <----1---->
cube = lambda var: var ** 3

# <----2---->
def decrement_list(list1):
    return list(map(lambda dec: dec - 1, list1))

# <----3---->
def remove_negatives(l):
    return list(filter(lambda num: num >= 0, l))

# <----3---->
# want to find name with length 3
names = ['Ayra', 'Samson', 'Dora', 'Tim', 'Ollivander']

max(names, key=lambda n: len(n))

def extremes(it):
    return (min(it), max(it))

# <----4---->
def max_magnitude(l):
    return max([abs(i) for i in l])

# <----5---->
def sum_even_values(*nums):
    return sum(i for i in nums if i % 2 == 0)

# <----6---->
def sum_floats(*nums):
    return sum(i for i in nums if type(i) == float)