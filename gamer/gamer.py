# def runner(a):
#             print('holaa numero ' + str(a))


# array = input("inserte the value: ")
# print(array)
# for e in array:
#             print(int(e))

            
# runner(array)

# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
#     while (x < 10):
#                       print(x, end=' ')
#                       x = x + 1


# for x in range(1, 11):
#               print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
#               print(repr(x*x*x).rjust(4))

# f = open('workfile', 'w')

# word = input("inserte the word:  ")
# counter = 0
# while (counter <= 10 ):
#     print(word)
#     counter = counter + 1

# word = input("inserte the word: ")
# for i in range(10):
#     print(word)



# name = input("what is your name? ")
# print("hello " + name)

# result = ((3+2)/(2*5))**2
# print(result)

# hour = int(input("how many hours you worked? "))
# price = int(input('what is the hour price?'))
# result = hour * price
# print("your payment is: ", int(result))

# sum = int(input("insert a number: "))
# for i in range(sum):
#     print(i + 1)


subject = []
sub = input("insert subjects: ")
finish = sub.split(',')
subject.append(finish)
print(subject)