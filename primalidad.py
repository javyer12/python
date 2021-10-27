# function to know if your number is prime or not
def is_prime(num):
  counter = 0

  for i in range(1, num+1):
    if i == 1 or i == num:
      continue
    if num % i == 0:
      counter += 1
  if counter == 0:
    return True
  else:
    return False


def run():
  num = int(input('Write down a number: '))
  if is_prime(num):
    print('The number is prime')
  else:
    print('The number is not prime')

if __name__ == '__main__':
  run()

