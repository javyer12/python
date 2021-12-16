import random
from collections import Counter

def run():
    word = input("Enter a list of letters: ")
    # comparation of words
    vowel = ["a", "e", "i", "o", "u"]
    not_allowed = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "?", ".", ",", ";", ":", "/", ">", "<", "|", "~", "`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    letters  = word.lower()

    while  3 < 6:
        word_complete = ''  
        # word_space = 6
        random_letter = random.choice(letters)
        print(random_letter)
        if 1 >  0:
            if(random_letter not in not_allowed ):
                word_complete.join(random_letter)
                print(random_letter)
                print(word_complete)
                # word_space -= 1
            else:
                break
        elif (word_complete != ''):
            if (word_complete[0] not in vowel):
                # if(word_space == 5):
                    if(random_letter  in vowel and random_letter not in not_allowed):
                        word_complete.join(random_letter)
                        print(word_complete)
                        # word_space -= 1
                    else:
                        break
            else:
                break
           
        print(word_complete)
        break
# USAR EL LOOP SWITCH

    # for i in range(6):
    #     attemps = 6
    #     option = ['a','b','c']
    #     if random_letter in vowel:
    #         print("The word starts with a vowel")
    #         print(random_letter)
    #         print(option)
    #         if random_letter in not_allowed:
    #             print("The letter is not allowed")
    #             print(random_letter)
    #         attemps -= 1
    #     else:
    #         print("The word starts with a consonant:  " + str(random_letter))
    #         attemps -= 1
    # new_word = []
    # let = 'esta es la= '
  
    # worddes = Counter(vowel)
    # for i in random_letter:
    #     if 5 < 6:
    #         if i in vowel:
    #             print("es una vocal")
    #             new_word.append(i)
    #         elif i in not_allowed:
    #              if new_word.length() >= 6 :
    #                  print("tienes: " + (new_word.index) + " de espacios")
    #         else:
    #             print("es una consonate...")
    #             new_word.append(i)
    #         print(new_word)
    #     else:
    #         print("no hay mas espacios")
    #         print(new_word)

    #     print(i)
    #     print(worddes['a'])
    #     print(  let.append(vowel))
# agrega un caracter a un string, pero al comienzo
        # print(let.join((vowel)))

#conocer la longitud de una cadena de texto
        # print(len(vowel))
#random_letter dentro del ciclo




if __name__ == '__main__':
  run()

#esto no se puede arreglar de otra menera