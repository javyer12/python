import random

def run():
    word = input("Enter a list of words: ")
    # comparation of words
    vowel = ["a", "e", "i", "o", "u"]
    not_allowed = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "?", ".", ",", ";", ":", "/", ">", "<", "|", "~", "`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    letters  = word.lower()

    random_letter = random.choice(letters)

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
    new_word = []
    for i in random_letter:
        if 5 < 6:
            if i in vowel:
                new_word.append(i)
            elif i in not_allowed:
                 if new_word.length() >= 6 :
                     print("tienes: " + (new_word.index) + " de espacios")
            else:
                print("es una consonate...")
                new_word.append(i)
            print(new_word)
        else:
            print("no hay mas espacios")
            print(new_word)

        print(i)

# arreglar que, el recorrido por las listas debe hacer aparte del codigo que se imprime, funciona, pero solo en un intento
# arreglar la longitud de la lista nueva, para saber cuantos espacios quedan





if __name__ == '__main__':
  run()

#esto no se puede arreglar de otra menera