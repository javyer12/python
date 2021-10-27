# code to get the factorial function

def run():
  num = input('Write down a number get its factorial: ')
  if num.isdigit():
    num = int(num)
    factorial = 1
    for i in range(1, num+1):
      factorial *= i
    print(f'The factorial of {num} is {factorial}')
  else:
    print('The number is not valid')
  # for i in range(num):

if __name__ == '__main__':
  run()