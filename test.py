'''my_str='Milk,Cottage,Cake,cake,Meat,Tomatoes,Bread,Cake,Oranges,Apple,Onion,Carrates,&fa,eg'
my_str = my_str.split( ',' )
print(my_str)

list2 = []

for product in my_str:
    not_legal_ch = False
    for ch in product:
        if not ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')) or (len( product ) < 3):
            not_legal_ch == True
            if product not in list2:
                list2.append( product )
if len( list2 ) > 0:
    print( list2, 'num' )
    print('\n\n\n')



secret_word = "mammals"
old_letters_guessed=['a','b','m','m','a']
guessed_word = "_ " * len( secret_word )
guessed_word.split("_")
def check_if_all_character_founds():
    for letter in old_letters_guessed:
        if letter in secret_word:
            index = secret_word.find( letter )
            if secret_word[ 2 * index ] != letter:
                guessed_word = guessed_word[ :2 * index ] + letter + guessed_word[ 2 * index + 1: ]
    print(guessed_word)

check_if_all_character_founds()
'''
d = dict(name = 'Elie', job = 'Instructor')

for k in d:
    print(k)

# name
# job


d = dict(name = 'Elie', job = 'Instructor')

for key, value in d.items():
    print(f"{key}:{value}")

# name:Elie
# job:Instructor


d = {'a': 1, 'c': 3, 'e': 5}
[v for k,v in d.items()] # [1, 5, 3]
[k for k,v in d.items()] # ['a', 'e', 'c']


num_list = [1,2,3,4]
print({ num:("even" if num % 2 == 0 else "odd") for num in num_list })

str1 = "ABC"
str2 = "123"
{str1[i]: str2[i] for i in range(0,len(str1))} # {'A': '1', 'B': '2', 'C': '3'}

x = (1,2,3)
3 in x # True
# x[0] = "change me!" # TypeError: 'tuple' object does not support item assignment

x = (1,2,3,3,3)
x.count(1) # 1
x.count(3) # 3


t = (1,2,3,3,3)
t.index(1) # 0
# t.index(5) # ValueError: tuple.index(x): x not in tuple
t.index(3) # 2 - only the first matching index is returned

# Sets cannot have duplictes
s = set({1,2,3,4,5,5,5}) # {1, 2, 3, 4, 5}

# Creating a new set
s = set({1,4,5})

# Creates a set with the same values as above
s = {4,1,5}

# True
4 in s

# False
8 in s

s = set([1,2,3])
s.add(4)
s # {1, 2, 3, 4}
s.add(4)
s # {1, 2, 3, 4}

s = set([1,2,3])
s.clear()
s # set()

s = set([1,2,3])
another_s = s.copy()
another_s # {1, 2, 3}
another_s is s # False

set1 = {1,2,3}
set2 = {2,3,4}
set1.difference(set2) # {1}
set2.difference(set1) # {4}

set1 = {1,2,3}
set2 = {2,3,4}
set1.intersection(set2) # {2,3}

set1 = {1,2,3}
set2 = {2,3,4}
set1.symmetric_difference(set2) # {1,4}

def foo(*args):
   print(args)

foo(1,2,3) # (1,2,3)
foo(1,2) # (1,2)
foo([1,2,3]) # ([1,2,3])

def add_and_multiply_numbers(a,b,c):
    return a + b * c

numbers = [1,2,3]
more_numbers = (4,5,6)

#add_and_multiply_numbers(numbers) # TypeError
add_and_multiply_numbers(*numbers) # 7

#add_and_multiply_numbers(more_numbers) # TypeError
add_and_multiply_numbers(*numbers) # 34



def print_kwargs(a,b,**kwargs):
    print(a,b,kwargs)

print_kwargs(1,2,awesome='sauce', test='yup') # 1 2 {'test': 'yup', 'awesome': 'sauce'



def add_and_multiply_numbers(a,b,c):
    return a + b * c

data = dict(a=1,b=2,c=3)

#add_and_multiply_numbers(data) # TypeError
add_and_multiply_numbers(**data) # 7



def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection

list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") # 1
list_manipulation([1,2,3], "add", "beginning", 20) # [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) # [1,2,3,30]


def difference(a,b):
    return a-b

def product(a,b):
    return a*b

def print_day(num):
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
    except IndexError as e:
        return None

def last_element(l):
    try:
        return l[-1]
    except IndexError as e:
        return None

def number_compare(a,b):
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    return "Numbers are equal"

def single_letter_count(string,letter):
    return string.lower().count(letter.lower())

def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}

def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection

def is_palindrome(string):
    return string == string[::-1]

def frequency(collection, searchTerm):
    return collection.count(searchTerm)

def flip_case(string, letter):
    return "".join([char.swapcase() if char.lower() == letter.lower() else char for char in string])

def multiply_even_numbers(list):
    # you can import reduce from the functools module if you would like
    total = 1
    for val in list:
        if val % 2 == 0:
            total = total * val
    return total

def mode(collection):
    # you can import mode from statistics to cheat
    # you can import Counter from collections to make this easier

    # or we can just solve it :)
    count = {val: collection.count(val) for val in collection}
    # find the highest value (the most frequent number)
    max_value = max(count.values())
    # now we need to see at which index the highest value is at
    correct_index = list(count.values()).index(max_value)
    # finally, return the correct key for the correct index (we have to convert cou)
    return list(count.keys())[correct_index]

def capitalize(string):
    return string[:1].upper() + string[1:]

def compact(l):
    return [val for val in l if val]

def partition(list, fn):
    return [[val for val in list if fn(val)], [val for val in list if not fn(val)]]

def intersection(l1, l2):
    return [val for val in l1 if val in l2]

def once(fn):
    fn.is_called = False
    def inner(*args):
        if not(fn.is_called):
            fn.is_called = True
            return fn(*args)
    return inner






from collections import Counter

l = [1,1,2,3,3,4,4,5,5]
Counter(l) # see what this returns!

string = "aweosakjdsaldwjdwq"
Counter(string)

s = 'this is such a nice nice nice thing that is nice!'

c = Counter(s.split())


d = {}
d['one'] = 1
d['two'] = 2
d['three'] = 3
d['four'] = 4

for k,v in d.items():
    print(k,v) # no order!


from collections import OrderedDict

od = OrderedDict()
od['one'] = 1
od['two'] = 2
od['three'] = 3
od['four'] = 4

for k,v in od.items():
    print(k,v) # order!


mylist = ['spam', 'ham', 'eggs']
print(' '.join(mylist))    #spam, ham, eggs

print ('\n'.join(mylist))
