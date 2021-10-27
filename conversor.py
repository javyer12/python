# code to change your currency

def conversor(type_currency, dollar_value):
        currency = float(input('Insert how much ' + type_currency + ' you have: '))
        dollars = currency / dollar_value
        dollars = round(dollars, 2)
        dollars = str(dollars)
        print('You have $' +dollars + ' dollars')

menu = """
Welcome to currency converter✨✨✨

1-Colombian pesos
2-Argentine pesos
3-Mexican pesos
4-Honduras Lempiras

take one:
"""

opcion = int(input(menu))

if opcion == 1:
       conversor('Colombian pesos', 3875)
elif opcion == 2:
       conversor('Argentine pesos',91)
        
elif opcion == 3:
       conversor('Mexican pesos', 20.4)
elif opcion == 4:
       conversor('Honduras Lempiras', 24)
       
else:
        print('Insert a right option')




