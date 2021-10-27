import random

def run():
  random_num = random.randint(1,100)
  choosen_num = int(input("Choose a number between 1 and 100: "))
  live = 5
  while choosen_num != random_num:
    if choosen_num < random_num:
      print("Too low")
      live -= 1
    elif choosen_num > random_num:
      print("Too high")
      live -= 1
    if live == 0:
      print("You lose🥴🥴")
      break
    print("Your lives is: ", live), 
    choosen_num = int(input("Choose another number: "))
    if choosen_num == random_num:
      print("You win!🎉🎉🎊🎉🎉🥳🥳")

if __name__ == '__main__':
  run()