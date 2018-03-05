# my solutions to the udemy functions exercises section
# <----1---->
def product(one, two):
    return one * two

# <----2---->
keys = {1: 'Sunday', 
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'
}

def return_day(day):
    answer = keys.get(day)
    if answer != "":
        return answer
    else:
        return 'None'

# <----3---->
def last_element(arg):
    if len(arg) > 0:
        return arg[len(arg) - 1]
    else:
        return None

# <----4---->
def number_compare(x, y):
    if x > y:
        return 'First is greater'
    elif x < y:
        return 'Second is greater'
    else:
        return 'Numbers are equal'

# <----5---->
def single_letter_count(string1, char1):
    count = 0
    for letter in string1:
        if letter.lower() == char1.lower():
            count += 1
    return count

# <----6---->
def multiple_letter_count(string1):
    answer = {letter: string1.count(letter) for letter in string1}
    return answer

# <----7---->
def list_manipulation(list1, command, location, value=0):
    if command == 'remove':
        if location == 'end':
            print(list1.pop(len(list1) - 1))
        elif location == 'beginning':
            print(list1.pop(0))
    elif command == 'add':
        if location == 'beginning':
            print(value)
            print(list1.insert(0, value))
            print(list1)
        elif location == 'end':
            print(list1.append(value))

# list_manipulation([1,2,3], "remove", "end") # 3
# list_manipulation([1,2,3], "remove", "beginning") #  1
# list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
# list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]

# <----8---->
def is_palindrome(string1):
    reverse = []
    for letter in string1:
        reverse.insert(0, letter.lower())
        
    reverse = ''.join(reverse)
    
    if string1 == reverse:
        return True
    else:
        return False

# is_palindrome('testing') # False
# is_palindrome('tacocat') # True
# is_palindrome('hannah') # True
# is_palindrome('robert') # False
# is_palindrome('amanaplanacanalpanama') # True

# <----9---->
def frequency(list1, search_term):
    count = 0
    for item in list1:
        if item == search_term:
            count += 1
    return count

# frequency([1,2,3,4,4,4], 4) # 3
# frequency([True, False, True, True], False) # 1

# Instructor Solution

def frequency(collection, searchTerm):
    return collection.count(searchTerm)

# <----10---->
def multiply_even_numbers(list1):
    product = 1
    for num in list1:
        if num % 2 == 0:
            product *= num
    return product

# <----11---->
def capitalize(string1):
    firstLetter = string1[0]
    return string1.replace(firstLetter, firstLetter.upper(), 1)

# <----13---->
def intersection(list1, list2):
    intersection = []
    for i in list1:
        for j in list2:
            if i == j:
                intersection.append(j)
                
    return intersection

# Other way
def intersection(list1, list2):
    return [val for val in list1 if val in list2]

# Third way - Most Efficient
def intersection(list1, list2):
    return [val for val in set(list1) and set(list2)]

# <----14---->
def partition(list1, callback):
    partition = [[],[]]
    for item in list1:
        if callback(item) == True:
            partition[0].append(item)
        else:
            partition[1].append(item)
            
    return partition

# Trying another way
def partition(list1, callback):
    return [[val for val in list1 if callback(val) == True], 
    [val for val in list1 if callback(val) == False]]