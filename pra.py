import random

def run():
    small_lett = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for i in range(5):
        word =  random.choice(small_lett)
        print(word)

word = 'b'
word1 = word + 'a'
word2 = word1 + word1
print(word2)

if __name__ == '__main__':
  run()