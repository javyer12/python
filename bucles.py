def run():
        LIMIT = 1000

        counter = 0
        potential_2 = 2**counter
        while potential_2 < LIMIT:
                print('2 raised to ' +  str(counter) + '  is equal to: ' + str(potential_2))
                counter += 1
                potential_2 = 2**counter


if __name__ == "__main__":
        run()
