# def fib (n):
#     a,b  = 0,100
#     while a < n :
#         print(a, end = ',')
#         a,b = b*2, b * (a-b)
#     print()

# # fib(1000)

# from typing import ValuesView


# def ask_ok(promt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(promt)
#         if ok in ('y', 'ye', 'yes'):
#                 return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#                 return False
#         retries = retries - 1
#         if retries < 0 :
#             raise ValuesView('invalid user response')
#         print(reminder)        

# ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?', 2)
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')


# i = 6
# def f(arg = i):
#     print(arg)
# i=5
# f()
# f(i + i)

z = ['a', 'b', 'c']
# list.extend()
# list.append()
# list.insert(3, 'd')
# list.remove()= remove the first item from the list
# list.pop()= remove then item in the position given
# z.clear()= remove all the items from the list
# z.count(x)= return how many time x is in the list
# z.reverse()= reverse all items in the list
# z.sort= sort all items in the list
# x = z.copy()
# y = ['holaa']
# x.append(y)
# print(x) = make a copy of the list

print(z)

