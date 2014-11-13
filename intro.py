# comments in python use the pound sign
# no need to put var before creating a variable
# no need for semicolons at the end
# can put integers or float
#use strings or double qoutes
#ctrl d to exit out of terminal
#ctrl k to clear

#chapter 3
# x = 3
# y = 4.2
# z = 'hello'
# a = "world"
# b = x + y - x
# c = 8 / 3
# d = 8 // 3 # will give you the whole number associated with the division
# e = 8 % 3
# f = 2 ** 2 # 2 to the power of 2
# g = z + ' ' + a
# h = 3 * 'un' + 'ium' #can multiply a number by a string
# i = 'Py' 'thon' #will concactinate to single string
# word = 'Python'
# list = [1,2,3,4,5]
# squares = list[:] + [6, 7, 8]
# squares.append(7**3)
# squares[:] = [] #clears an array
#
#
# a, b = 0, 1
# while b < 100: #: signifies the end
#     print(b, end=',') #will print sequence in line separated by commas until the end
#     a, b = b, a+b
#
#
#
# print(x, y, z, a, b, c, d, e, f, g, h, i, word[0], word[-1], word[:2], word[2:], len(word), squares)
# print('C:\some\name')
# print(r'C:\some\name')

############################################

######## if else statements ###############

# x = int(input("Please enter an integer"))
#
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')


############lists######################

#Measure some strings:

# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))

# for w in words[:]: #loop over a slice copy of an entire list
#     if len(w) > 6:
#         words.insert(0, w)
#         print(words)

##############range and for loops##################

# for i in range(5, 10):
#     print(i)

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])
#
# # seasons = ['spring', 'summer', 'winter', 'fall'] #will give index with each list item
# # list(enumerate(seasons))
#
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else: #loop fell through without find a factor
#         print(n, 'is a prime number')


#################pass######################

# while True:
#     pass #busy-wait f or keyboard interrupt (Ctrl+C)
#
# class MyEmptyClass:
#     pass
#
# def initlog(*args):
#     pass #Remember to implement this

#######defining functions#############

# def fib(n): #write Fibonacci series up to n
#     """Print a Fibonacci series up to n."""
#     a, b = 0,1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()
#
# fib(2000)
#
# f = fib
# f(3000)
#
# print(f(0))
#
# def fib2(n):
#     result = []
#     a, b = 0,1
#     while a < n:
#         result.append(a)
#         a, b = b, a+b
#     return result
#
# fib100 = fib2(100)
# print(fib100)
#
# def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'y', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries -1
#         if retries < 0:
#             raise IOErro('uncooperative user')
#         print(complaint)
#
# ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?', 2)
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

#
# i = 5
#
# def f(arg=i):
#     print(arg)
#
# i = 6
# f()
#
# def f(a, L=None):
#     if L is None:
#         L=[]
#     L.append(a)
#     return L
#
# print(f(1))
# print(f(2))
# print(f(3))
#
# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")
#
# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
#
# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     keys = sorted(keywords.keys())
#     for kw in keys:
#         print(kw, ":", keywords[kw])
#
# cheeseshop("limburger", "it's very runny, sir",
#             "it's really very, VERY runny, sir.",
#             shopkeeper = "Michael Palin",
#             client ="John Cleese",
#             sketch = "cheese shop sketch")


####inclass#####

age = 20
gender = 'female'

if age>=21 and (gender == 'female' or gender =='male'):
    print('go drink')
else:
    print('go drink anyway')

for x in range(20, -50,-5):
    print("{0} to the {1} power is {2}".format(x, 2, x**2))
