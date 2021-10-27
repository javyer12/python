def run():
  for contador in range(10):
    if contador % 2 != 0:
      continue
    print(contador)
  
  for i in range(10000):
    print(i)
    if i == 0:
      break

  text =  input('escribe un texto: ' )
  for letter in text:
    if letter == 'o':
      break
    print(letter)
  
  text = input('escribe un text: ' )
  for punto in text:
    if punto == ',':
      continue
    print(punto)
    if punto == '.':
        break
    print(punto)


