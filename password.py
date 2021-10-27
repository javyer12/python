# code to generate a random password
import random

def get_password():
    capital_lett = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    small_lett = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    symbols = ['!','@','#','$','%','^','&','*','(',')','_','+','=','{','}','[',']','|',':',';','"','<','>','?','~','`','.','/']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    characters =capital_lett + small_lett + symbols + numbers
    password = []

    for i in range(15):
      passor = random.choice(characters)
      password.append(passor)

    password = ''.join(password)
    return password


def run():
  password = get_password()
  print('Your password is: ' + str(password))

if __name__ == "__main__":
  run()