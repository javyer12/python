def palindrome(word):
        word = word.replace(' ', '_')
        word = word.lower()
        inverted_word = word[::-1]
        if word == inverted_word:
                return True
        else:
                return False


def run():
        sentence = input('write down a word or sentence: ')
        is_palindrome = palindrome(sentence)
        if is_palindrome == True:
                print('Is Palindrome')
        else:
                print('Its not Palindrome')


if __name__ == '__main__':
        run()